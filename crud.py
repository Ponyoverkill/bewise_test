from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import send_request
from schemas import Question, Category
from models import Question as Quest, Category as Cat


async def add_cat(db: AsyncSession, category: Category) -> None:
    '''
    Create or update category in DB
    :return None
    '''
    cat = Cat(**category.model_dump())
    exist_cat = await db.get(Cat, cat.id)

    if exist_cat is None:
        db.add(cat)
        await db.commit()
    elif exist_cat is not None and exist_cat.updated_at != cat.updated_at:
        query = update(Cat).where(Cat.id == cat.id).values(
            title=cat.title,
            updated_at=cat.updated_at
        )
        await db.execute(query)
        await db.commit()


async def add_question(db: AsyncSession, question: Question) -> Question:
    '''
    Create or update question in DB.
    If question already in DB and not updated, then get new question by send_request() and
    call add_questions
    '''

    quest = Quest(**question.model_dump(exclude={'category'}))
    quest.category_id = question.category.id

    exist_quest = await db.get(Quest, quest.id)

    if exist_quest is None:
        db.add(quest)
        await db.commit()
        return question
    elif exist_quest is not None and exist_quest.updated_at != quest.updated_at:
        query = update(Quest).where(Quest.id == quest.id).values(
            answer=quest.answer,
            question=quest.question,
            updated_at=quest.updated_at,
            category_id=quest.category_id
        )
        await db.execute(query)
        await db.commit()
        return question
    else:
        questions = await send_request(questions_num=1)
        return await add_questions(db, questions)


async def add_questions(db: AsyncSession, questions: list[Question]) -> Question:
    for quest in questions:
        await add_cat(db, quest.category)
        q = await add_question(db, quest)
    return q
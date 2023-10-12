import httpx
from pydantic import ValidationError

from schemas import Question
from config import JSERVICE_URL


async def send_request(questions_num: int) -> list[Question]:
    async with httpx.AsyncClient() as client:
        response = await client.request(method='GET',
                                        url=JSERVICE_URL,
                                        params={'count': questions_num})
    result = response.json()
    questions = []
    for item in result:
        try:
            questions.append(Question.model_validate(item))
        except ValidationError as e:
            return e
    return questions

import json

from fastapi import FastAPI, Depends
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from database import get_async_session
from dependencies import send_request
from schemas import Question
from crud import add_questions

app = FastAPI()


@app.post('/question')
async def question(
        items: list[Question] = Depends(send_request),
        db: AsyncSession = Depends(get_async_session)
                   ):
    if isinstance(items, ValidationError):
        return JSONResponse(items.errors(), status_code=422)
    last_question = (await add_questions(db, items)).model_dump_json()
    return JSONResponse(json.loads(last_question), status_code=200)

from crud import get_questions
@app.get('/questions')
async def questions(count: int, db: AsyncSession = Depends(get_async_session)):

    return await get_questions(db, count)

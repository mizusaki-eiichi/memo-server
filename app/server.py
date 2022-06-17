from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn

from cruds.m_memo import create_memo_by_m_memo, get_memos_by_m_memo
from lib.database import Base, engine, get_db
from schemas.schemas import MemoCreatingSchema, MemoSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/read_memos", response_model=List[MemoSchema])
async def read_memos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    memos = get_memos_by_m_memo(db, skip=skip, limit=limit)
    return memos


@app.post("/create_memos", response_model=MemoCreatingSchema)
async def create_memo(memo: MemoCreatingSchema, db: Session = Depends(get_db)):
    return create_memo_by_m_memo(db=db, memo=memo)

if __name__ == "__main__":
    uvicorn.run(app=app)

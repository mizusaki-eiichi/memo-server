from sqlalchemy.orm import Session

from models.models import Memo
from schemas.schemas import MemoCreatingSchema


def get_memos_by_m_memo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Memo).offset(skip).limit(limit).all()


def create_memo_by_m_memo(db: Session, memo: MemoCreatingSchema):
    db_memo = Memo(content=memo.content)
    db.add(db_memo)
    db.commit()
    db.refresh(db_memo)
    return db_memo

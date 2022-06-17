from datetime import datetime

from sqlalchemy import Column, DATETIME, Integer, String

from lib.database import Base


M_MEMO = 'm_memo'


class BaseColumn(Base):
    __abstract__ = True

    create_user_id = Column(String(13), default="admin")
    created_at = Column(DATETIME, default=datetime.now)
    update_user_id = Column(String(13), default="admin")
    updated_at = Column(DATETIME, default=datetime.now)


class Memo(BaseColumn):
    __tablename__ = M_MEMO

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, index=True)

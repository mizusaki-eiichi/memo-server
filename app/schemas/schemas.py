from pydantic import BaseModel, Field


class MemoSchema (BaseModel):
    id: int = Field()
    content: str = Field(max_length=100)

    class Config:
        orm_mode = True


class MemoCreatingSchema (BaseModel):
    content: str = Field(max_length=100)

    class Config:
        orm_mode = True

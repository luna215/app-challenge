from pydantic import BaseModel

class DocumentBase(BaseModel):
    title: str
    author: str

    class Config:
        orm_mode = True


class CreateDocument(DocumentBase):
    pass
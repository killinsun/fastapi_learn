from pydantic import BaseModel, Field


class DoneResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, Field


class Model(BaseModel):
    mol: str
    lom: int


class ModelOut(BaseModel):
    full: str = Field(description="Summa")

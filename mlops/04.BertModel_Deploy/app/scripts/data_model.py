# pydantic
from pydantic import BaseModel

def BertInput(BaseModel):
    text: list[str]

def BertOutput(BaseModel):
    model_name:str
    text: list[str]
    labels: list[str]
    scores: list[str]
    prediction_time: int    # 초 데이터
    
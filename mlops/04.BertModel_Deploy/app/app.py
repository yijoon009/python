from fastapi import FastAPI
import os
from scripts import s3
import torch
from transformers import pipeline

from scripts.data_model import BertInput, BertOutput

app = FastAPI()

# Model Download
model_name = 'tinybert-sentiment-analysis'
local_path = 'ml-models/'+ model_name # 아까 생성한 s3 버킷명과 동일하게 세팅해줬다.

if not os.path.isdir(local_path):
    # s3 버킷에 업로드된 모델을 다운로드
    s3.download_dir(local_path, model_name)


# Model Load
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = pipeline('text-classification', model=local_path, device=device)



@app.get('/')
def index():
    return {'hello':'fastapi'}

# Rest API 에서 input, output 정의해줘야한다. 정의하는 이유는 data type 체크 위해서! (궁극적으로는 text만 받기 위해서) => Pydantic 사용
@app.post('/api/v1/sentiment')
def sentiment_analysis(data: BertInput):
    pass
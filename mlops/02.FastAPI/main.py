from fastapi import FastAPI, UploadFile, File # socket => chatting | AI Chatbot | AI Agent(CrewAI)
# AutoGPT => 추론모델 o1 => GPT 매니지먼트(관리감독)
from io import BytesIO
from PIL import Image
from predict import predict

app = FastAPI()

@app.get('/')
def index():
    return {"Hello":"World!"}

@app.get('/api/v1/users/{user_name}') # wireshark: api
def get_user(user_name):
    return {'user_name':user_name}

@app.get('/api/v1/predict')
async def image_predict(file: UploadFile = File(...)): # input: Image
    raw_data = await file.read()
    image_bytes_io = BytesIO(raw_data)
    img = Image.open(image_bytes_io)
    pred = predict(img)
    return pred

    # return # output: predict

# uvicorn main:app --reload
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app) -  wsgi vs asgi

# model serving => Flask, FastAPI
# 모델을 불러와서 API 형태로 내려주는 연습
# docker 기반으로 서버 세팅하는 법 + GitHub Actions
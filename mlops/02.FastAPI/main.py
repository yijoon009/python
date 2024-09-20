from fastapi import FastAPI


# model serving -> Flask, FastAPI 
# 모델을 불러와서 API 형태로 내려주는 연습
# docker 기반으로 서버 세팅하는 법 + GitHub Actions

app = FastAPI()

@app.get('/')
def index():
    return {"hello': 'world"}

# uvicorn main:app
# 이 코드 대신에 python main.py 하려면 아래 코드 주석 해제해야함.
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app)  # wsgi vs asgi
import requests


class DataFetcher():
    def __init__(self, api_key: str, city: str):
        self.api_key = api_key
        self.city = city

    def fetch_weather(self):
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.api_key}'
        res = requests.get(url=url)
        # eval 함수는 주어진 글자를 파이썬 문법대로 parsing해서 실행하는 함수
        data = eval(res.content)
        return data

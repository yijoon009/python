import requests


class DataFetcher():
    def __init__(self, api_key: str, city: str):
        self.api_key = api_key
        self.city = city

    def fetcher_weather(self):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}'
        res = requests.get(url=url)
        # eval 함수는 주어진 글자를 파이썬 문법대로 parsing해서 실행하는 함수
        data = eval(res.content)
        return data

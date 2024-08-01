import requests

class DataFetcher:
    def __init__(self, API_KEY, city) -> None:
        self.api_key = API_KEY
        self.city = city

    def fetch_weather(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"  # Geocoding API
        res = requests.get(url=url)
        data = eval(res.content)  # eval 함수는 주어진 글자를 파이썬 문법대로 parsing해서 실행하는 함수.
        return data
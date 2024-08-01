from data_fetcher import DataFetcher
from data_processor import DataProcessor
from visualizer import Visualizer
# from logger import Logger
import requests


def main():
    api_key = ""
    city = input('which city? ')

    # fetcher는 api key와 city를 입력받아서 dict(원본) 넘기기
    fetcher = DataFetcher(api_key, city)
    # processor는 원본데이터(dict)를 입력받아서, 현재 온도가 5개 포함된 리스트를 return
    processor = DataProcessor()
    visualizer = Visualizer()
    # logger = Logger()

    raw_data = fetcher.fetch_weather()
    date, temp = processor.process_data(raw_data)
    print('>>>')
    print(date, temp)
    # logger.save_data(date, temp)
    visualizer.plot_data(date, temp)


if __name__ == "__main__":
    main()

from data_fetcher import DataFetcher
from data_processor import DataProcessor
from visualizer import Visualizer
# from logger import Logger
import requests


def main():
    api_key = "b8296554c33187ee32c819067c51fc37"
    city = input('which city? ')


    # fetcher는 api key와 city를 입력받아서 dict(원본) 넘기기
    fetcher = DataFetcher(api_key, city)
    # processor는 원본데이터(dict)를 입력받아서, 현재 온도가 5개 포함된 리스트를 return
    processor = DataProcessor()
    visualizer = Visualizer()
    # logger = Logger()

    # raw_data_list = []
    # for i in range(5):
    #     raw_data_list.append(fetcher.fetcher_weather())
    raw_data = [fetcher.fetcher_weather() for i in range(5)]
    processed_data = processor.process_data(raw_data)
    # logger.save_data(processed_data)
    visualizer.plot_data(processed_data)


if __name__ == "__main__":
    main()

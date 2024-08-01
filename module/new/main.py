from data_fetcher import DataFetcher
from data_processor import DataProcessor
from visualizer import Visualizer
from logger import Logger

def main():
    API_KEY = ""
    city = input("Which city? ")  # Seoul, Tokyo, Paris, London, ...

    # fetcher API_KEY와 city를 입력받아서, dict return (원본 데이터)
    fetcher = DataFetcher(API_KEY, city)
    # processor는 원본 데이터(dict)를 입력받아서, 현재 온도가 5개 포함된 리스트를 return.
    processor = DataProcessor()
    visualizer = Visualizer()
    # logger = Logger()
    
    raw_data = [fetcher.fetch_weather() for i in range(5)]
    processed_data = processor.process_data(raw_data)
    # logger.save_data(processed_data)
    visualizer.plot_data(processed_data)

if __name__ == '__main__':
    main()
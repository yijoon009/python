class DataProcessor:
    def __init__(self) -> None:
        pass

    def process_data(self, data):
        ## TO-DO ##
        processed_data = [content['main']['temp']-273 for content in data]
        return processed_data
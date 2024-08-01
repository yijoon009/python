class DataProcessor:
    def process_data(self, raw_data_list: list):
        curr_temp_list = []
        for raw_data in raw_data_list:
            curr = raw_data['main']['temp']
            curr_temp_list.append(f'{curr - 273:.2f}')
        return curr_temp_list

class DataProcessor:
    def process_data(self, raw_data: list):
        dates = []
        temps = []
        for entry in raw_data['list']:
            print('entry>>> ', entry)
            dates.append(entry['dt_txt'])
            temps.append(entry['main']['temp'] - 273.15)
        return dates, temps
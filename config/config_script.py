import configparser

config = configparser.ConfigParser()
config.sections()

config.read('example.cfg')
print(config.sections())

for key in config['SectionOne']:
    value = config['SectionOne'][key]
    print(f'{key}: {value}')

# print(config['SectionOne']['Status'])
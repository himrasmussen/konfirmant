import pprint
import os
def import_all_country_data():
    global country_data
    for country_data_txt in os.listdir('.'):
        if country_data_txt.endswith('.txt'):
            raw_data = open(country_data_txt).read().splitlines()
            country = country_data_txt[:-4]
            country_data[country] = {}
            for line in raw_data:
                if line:
                    key = line.split(':')[0]
                    values = line.split(':')[1].split(',')
                    country_data[country][key] = values


country_data = {}
import_all_country_data()
pprint.pprint(country_data)

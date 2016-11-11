import pprint
import os
def import_all_country_data():
    country_data = {}
    os.chdir("country_data")
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
    return country_data



if __name__ == "__main__":
    print(import_all_country_data())

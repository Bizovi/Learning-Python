# an introduction to classes and oop
# django in a nutshell ORM (DB->Py.Ojbects)
import pandas as pd
import csv
import requests

# Solve the problem via pandas
class GetGooglFinance:

    def __init__(self, url):
        self.url = url

    def get_google_finance(self):
        '''Use pandas to get stock market data'''
        data = pd.read_csv(self.url, skiprows=8, header=None)
        data.columns = ['DATE', 'CLOSE', 'HIGH', 'LOW', 'OPEN']
        return data


class WriteToCsv:

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, data):
        '''Use pandas to write to csv'''
        data.to_csv(self.filename)
        print('Writing to file successful')


# Solve the problem via bruteforce
# TO Be done: parametrize the call to the API
class GetDataBasic():

    def __init__(self, url):
        self.url = url

    def get_google_finance(self):
        '''Use the requests package to download the raw data/text'''
        response = requests.get(url=self.url)
        content = response.text
        return str(content)


class WriteBasic():

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, data):
        '''
        Use the csv module to write the data line b line
        First split by newrow, second split by line
        '''
        with open(self.filename, 'w') as file:
            writer = csv.writer(file)
            for line in data.split('\n'):
                writer.writerow(tuple(line.split(','))) # demands a tuples
        print('Done!')


if __name__ == '__main__':

    url = 'https://www.google.com/finance/getprices?q={}&x={}&i={}&p={}&f={}&df={}&auto={}&ts={}'
    url = url.format('RELIANCE', 'NSE', '60', '5d', 'd,c,o,h,l', 'cpct', '1', '1266701290218')
    stck = GetDataBasic(url)
    print(stck.__dict__)

    data = stck.get_google_finance()
    print(data)

    writer = WriteBasic('stock_raw.csv')
    writer.write_to_csv(data)

    print('\n')
    stock = GetGooglFinance(url)
    print(stock.__dict__)
    data = stock.get_google_finance()
    print(data.head())
    writer = WriteToCsv('stock_data.csv')
    writer.write_to_csv(data)

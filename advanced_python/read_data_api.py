# an introduction to classes and oop
# django in a nutshell ORM (DB->Py.Ojbects)
import pandas as pd
import csv
import requests

## Requirements for second week
# fix reading from csv
# 0. Rename WriteToCsv in ReadWriteFromToCsv
# 1. Create a class stockitem with attributes google finance params passed
# 2. Read the csv and return stockitem class
# 3. Adaugare de alta metoda la aceasta clasa ReadWriteFromToCsv care de
#   data aceasta citeste csv-ul creat si returneaza un set de obiecte de tip StockItem
# 4. Modificam local CSV-ul
# 5. La clasa GetGoolgleFinance adaugam alta metoda get_google_finance_return_set
#    care la fel ca get_google_finance face requestul doar ca returneaza un set de tip StockItem
# 6. Facem diff intre 3 si 5 si printam ce e modificat

class StockItem():

    def __init__(self, data):
        self.data = data


# Solve the problem via pandas
class GetGooglFinance:

    def __init__(self, url):
        self.url = url

    def get_google_finance(self):
        '''Use pandas to get stock market data'''
        data = pd.read_csv(self.url, skiprows=8, header=None)
        data.columns = ['DATE', 'CLOSE', 'HIGH', 'LOW', 'OPEN']
        return data

    def get_google_finance_stock(self):
        data = pd.read_csv(self.url, skiprows=8, header=None)
        data.columns = ['DATE', 'CLOSE', 'HIGH', 'LOW', 'OPEN']
        row_list = [data.columns, data.apply(lambda x: x.tolist(), axis=1)]
        return StockItem(row_list)

class WriteToCsv:

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, data):
        '''Use pandas to write to csv'''
        data.to_csv(self.filename)
        print('Writing to file successful')

    def read_from_csv(self):
        with open(self.filename) as file:
            readcsv = csv.reader(file, delimiter=',')
            items = []
            for row in readcsv:
                items.append(row)
        return StockItem(items)



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
            list_lines = data.split('\r\n')
            for line in list_lines: # split on chache return
                writer.writerow(line.split(',')) # demands a tuples
        print('Done!')


if __name__ == '__main__':

    fn = WriteToCsv('stock_data.csv')
    data = fn.read_from_csv().data
    # print(data.data)

    url = 'https://www.google.com/finance/getprices?q={}&x={}&i={}&p={}&f={}&df={}&auto={}&ts={}'
    url = url.format('RELIANCE', 'NSE', '60', '5d', 'd,c,o,h,l', 'cpct', '1', '1266701290218')
    # stck = GetDataBasic(url)
    # print(stck.__dict__)
    #
    # data = stck.get_google_finance()
    # print(data)
    #
    # writer = WriteBasic('stock_raw.csv')
    # writer.write_to_csv(data)
    #
    # print('\n')
    stock = GetGooglFinance(url)
    data_api = stock.get_google_finance_stock().data

    print(data_api[1:10])
    print(data[1:10])
    # print(stock.__dict__)
    # data = stock.get_google_finance()
    # print(data.head())
    # writer = WriteToCsv('stock_data.csv')
    # writer.write_to_csv(data)

# check dataset from yahoo finance vs local csv
import read_data_api as rd


if __name__ == '__main__':
    url = 'https://www.google.com/finance/getprices?q={}&x={}&i={}&p={}&f={}&df={}&auto={}&ts={}'
    url = url.format('RELIANCE', 'NSE', '60', '5d', 'd,c,o,h,l', 'cpct', '1', '1266701290218')
    stck = rd.GetGooglFinance(url)
    print(stck.__dict__)

    data = stck.get_google_finance()
    print(data[1:300])
    print(type(data)) # print(data)

    writer = rd.WriteToCsv('stock_data.csv')
    writer.write_to_csv(data)

import requests
import csv


class GoogleFinance(object):

    def __init__(self, url):
        self.url = url

    def download_data(self, q, x, i, p, f, df, auto, ts):
        url = "{}q={}&x={}&i={}&f={}&df={}&auto={}&ts={}".format(
            self.url, str(q), str(x), str(i),
            str(p), str(f), str(df), str(auto), str(ts))
        page = requests.get(url)
        return page.text


class ToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, data):
        with open(self.filename, "w") as csv_file:
            writer = csv.writer(csv_file)
            for i in data.split('\n'):
                writer.writerow(tuple(i.split(',')))


if __name__ == "__main__":
    a = GoogleFinance('https://www.google.com/finance/getprices?')
    data = a.download_data(
        'RELIANCE', 'NSE', '60', '5', 'd,c,o,h,l', 'cpt', 1, 1266701290218)
    print(data)

    b = ToCsv('test.csv')
    b.write_to_csv(data)

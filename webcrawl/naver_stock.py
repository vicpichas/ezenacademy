from bs4 import BeautifulSoup
from urllib.request import urlopen

class StockModel:
    def __init__(self, item):
        self.item = item

    def scrap(self):
        url = 'https://finance.naver.com/item/sise_day.nhn?code={code}'.format(code = self.item)

        # class="tah p11"
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        print('출력')

        for i in soup.find_all(name = 'span', attrs=({'class':'tah p11'})):



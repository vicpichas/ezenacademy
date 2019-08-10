from bs4 import BeautifulSoup
from selenium import webdriver


class NaverMovie:
    def __init__(self, url):
        drive = webdriver.Chrome(executable_path='C:\Users\user02\PycharmProjects\tensorflow_190806\webcrawl\data')
        self.driver.get(url)
        self.soup = BeautifulSoup(driver.page_source, 'htmp.parser')

    def scrap(self):
        html = self.soup.prettify()
        # print(html)
        all_divs = self.soup.find_all('div', attrs = {'class':'tit3'})
        print(all_divs)
        arr = [div.a.sting for div in all_divs]
        for i in arr:
            print(i)
        self.dirver.close()

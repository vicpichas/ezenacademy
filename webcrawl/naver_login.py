from bs4 import BeautifulSoup
from selenium import webdriver


class NaverLogin:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='https://nid.naver.comnidlogin.login)
            self.driver.implicitly_wait(3)
            self.driver.get(url)


    def autologin(self):
        self.driver.find_element_by_name('id').send_keys('*****')
        self.driver.find_element_by_name('pw').send_keys('*****')
        self.driver.implicity_wait(3)

        self.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(3)

        self.driver.get('https://order.pay.naver.com/home')
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        notices = soup.select('div.p_inr > div.p_info >a> span')
        for i in notices:
            print(i.text.strip()))
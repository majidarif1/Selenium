from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class DemoFindElementById():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        link_element = driver.find_elements(By.TAG_NAME, 'a')
        for i in link_element:
            print(i.text)

        #driver.find_element(By.LINK_TEXT, 'Yatra for Business').click()
        time.sleep(10)

d1 = DemoFindElementById()
d1.locate_by_id_demo()

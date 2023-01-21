from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoJs():
    def demo_Javascript(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver.get('https://www.rcvacademy.com/')
        driver.execute_script("window.open('https://www.rcvacademy.com/', '_self') ")
        time.sleep(4)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[2];")
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(5)


js = DemoJs()
js.demo_Javascript()
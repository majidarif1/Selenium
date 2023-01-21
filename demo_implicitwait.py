from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoImplicitWait():
    def demo_implicit(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://login.salesforce.com/?locale=in')
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "username").send_keys("Majid")

iwait = DemoImplicitWait()
iwait.demo_implicit()
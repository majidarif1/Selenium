from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Demo_gettext():
    def demo_get_text(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        text = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)").text
        print(text)
        time.sleep(2)

d1 = Demo_gettext()
d1.demo_get_text()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementById():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element('id','login-input').send_keys('abc@test.com')
        time.sleep(4)

d1 = DemoFindElementById()
d1.locate_by_id_demo()

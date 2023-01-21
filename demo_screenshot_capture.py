from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoScreenshot():
    def demo_screenshot_capture(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')

        continue_button = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continue_button.screenshot(".\\test.png")
        continue_button.click()
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\Users\\MAJID ARIF\PycharmProjects\\error.png")
        driver.save_screenshot(".\\test1.png")

screen = DemoScreenshot()
screen.demo_screenshot_capture()
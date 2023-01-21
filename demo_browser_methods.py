from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class DemoSeleniumLearning():
    def demo_browser_methods(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://training.rcvacademy.com')
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > header:nth-child(2) > nav:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
        time.sleep(4)
        driver.back()
        time.sleep(4)
        driver.forward()
        time.sleep(4)
        driver.minimize_window()
        time.sleep(6)
        driver.quit()

d1 = DemoSeleniumLearning()
d1.demo_browser_methods()
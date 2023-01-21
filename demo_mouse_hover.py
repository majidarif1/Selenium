from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoMouseHover():
    def demo_mouse(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        driver.maximize_window()

        more_button = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        my_acc = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        achains = ActionChains(driver)
        achains.move_to_element(my_acc).perform()
        time.sleep(4)
        achains.move_to_element(more_button).perform()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='Freight']").click()
        time.sleep(4)

dmousehover = DemoMouseHover()
dmousehover.demo_mouse()
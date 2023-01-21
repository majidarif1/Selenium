from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoDragDrop():
    def demo_drag_drop(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://jqueryui.com/droppable/')
        driver.maximize_window()

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.ID, "draggable")
        elem2 = driver.find_element(By.ID, "droppable")
        #ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1, 50, 40).perform()
        time.sleep(4)

dd = DemoDragDrop()
dd.demo_drag_drop()
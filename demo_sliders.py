from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoSlider():
    def slider_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.snapdeal.pk/phones/mobile-phones')
        driver.maximize_window()
        elem1 = driver.find_element(By.XPATH, "//input[@id='RangeMin']")
        elem2 = driver.find_element(By.XPATH, "//input[@id='RangeMax']")
        #ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 0).perform()
        #ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(100, 0).release().perform()
        ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80, 0).release().perform()
        time.sleep(4)

dslider = DemoSlider()
dslider.slider_demo()
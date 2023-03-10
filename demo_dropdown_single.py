from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Demo_dropdown_single_select():
    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.salesforce.com/in/form/signup/freetrial-sales/?d=jumbo1-btn-ft')
        dropdown = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)

        dd.select_by_value("CxO_General_Manager_AP")
        time.sleep(3)

dddemo = Demo_dropdown_single_select()
dddemo.demo_dropdown()

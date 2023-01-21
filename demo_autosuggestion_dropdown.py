from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoAutosuggestion():
    def demo_autodropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        going_to = driver.find_element(By.XPATH, "(//input[@id='BE_flight_arrival_city'])[1]")
        going_to.send_keys("New")
        time.sleep(4)
        searched_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(searched_result))
        for result in searched_result:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break

        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(5)

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper'\]//tbody//td[@class!='inActiveTD']")
        for dates in all_dates:
            if dates.get_attribute("data-date") == "25/01/2023":
                dates.click()
                time.sleep(5)
                break





dauto = DemoAutosuggestion()
dauto.demo_autodropdown()


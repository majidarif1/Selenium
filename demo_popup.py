from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoPopup():
    def demo_js_popup(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt')
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")


        # Accept alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(4)
        # driver.switch_to.alert.accept()
        # time.sleep(2)

        # Dismiss Alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(4)
        # driver.switch_to.alert.dismiss()
        # time.sleep(2)

        # Send Keys
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(4)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Majid")
        driver.switch_to.alert.accept()
        time.sleep(2)

popup = DemoPopup()
popup.demo_js_popup()


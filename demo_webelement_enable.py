from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Demo_webelementenable():
    def demo_enabled(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://training.openspan.com/login')
        demo_state = driver.find_element(By.ID, "login_button").is_enabled()
        print(demo_state)
        driver.find_element(By.ID, "user_name").send_keys("abc@test.com")
        time.sleep(2)
        driver.find_element(By.ID, "user_pass").send_keys("123456")
        time.sleep(2)
        demo_state1 = driver.find_element(By.ID, "login_button").is_enabled()
        print(demo_state1)

        time.sleep(2)

d1 = Demo_webelementenable()
d1.demo_enabled()
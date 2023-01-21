from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select


class DemoMultiwindow():
    def demo_windows(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://yatra.com')
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()
        time.sleep(5)

        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.CSS_SELECTOR,
                                    "body > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span:nth-child(4) > span:nth-child(3) > span:nth-child(1)").click()
                time.sleep(5)
                driver.close()
                time.sleep(5)
                break
        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()



multi = DemoMultiwindow()
multi.demo_windows()
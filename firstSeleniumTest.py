from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#s = Service("C:\\browserdrivers\\chromedriver.exe")

#driver = webdriver.Chrome(service=s)

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
#driver.close()




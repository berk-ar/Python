from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#service = Service(executable_path="C:\+++LocalFile\chromedriver\chromedriver.exe")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://google.com")
print(driver)

time.sleep(5)
driver.fullscreen_window()
time.sleep(5)

driver.quit()
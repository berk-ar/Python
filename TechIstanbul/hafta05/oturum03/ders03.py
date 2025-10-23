"""
Web Elementlerini Bulma Yöntemleri
📌 2.1 Element Bulma Stratejileri
Selenium, HTML elementlerini bulmak için 8 temel yöntem sunar:

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.CLASS_NAME, "class")
find_element(By.TAG_NAME, "div")
find_element(By.XPATH, "//input[@name='q']")
find_element(By.CSS_SELECTOR, "input[name='q']")
find_element(By.LINK_TEXT, "Gmail")
find_element(By.PARTIAL_LINK_TEXT, "Gma")
⚠️ By modülünü import etmeyi unutmayın: 

python

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://google.com")


arama_kutusu = driver.find_element(By.NAME, "q")
driver.implicitly_wait(10)  # Sayfanın yüklenmesi
time.sleep(5)   # Sistemin beklemesi
arama_kutusu.send_keys("github")
arama_kutusu.submit()
time.sleep(5)
driver.implicitly_wait(10)
print(driver.title)

driver.quit()
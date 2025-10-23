from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

def setup_driver():
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")   # Açılan ekran büyük
    options.add_argument("--disable-noifications")  # Bildirimleri devre dışı bırakır

    driver = webdriver.Chrome(service = service, options = options)

    driver.implicitly_wait(10)

    return driver

def selenium_test_1():
    driver = setup_driver()

    try:
        driver.get("https://google.com")

        arama_kutusu = driver.find_element(By.NAME, "q")

        driver.implicitly_wait(10)  # Sayfanın yüklenmesi
        time.sleep(5)   # Sistemin beklemesi

        arama_kutusu.send_keys("github")
        arama_kutusu.submit()

        time.sleep(5)
        driver.implicitly_wait(10)

        print(driver.title)

        driver.implicitly_wait(10)

        # driver.save_screenshot("c:/PythonEdu/Python/TechIstanbul/hafta05/oturum03/test.png")

        time.sleep(5)
    except Exception as e:
        print("Hata:",e)
    finally:
        print("Tarayıcı kapatıldı.")
        driver.quit()

selenium_test_1()
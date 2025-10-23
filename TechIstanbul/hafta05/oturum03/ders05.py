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

def selenium_test_2():
    driver = setup_driver()

    try:
        driver.get("https://www.hepsiburada.com")
        time.sleep(3)
        try:
            # Sayfada çerez kabul etme
            kabul_et_butonu = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            kabul_et_butonu.click()

            print("Çerezler kabul edildi.")
        except Exception as e:
            print("Çerezler kabul edilmedi, Hata:", e)

        time.sleep(5)
        driver.implicitly_wait(10)

        # element = driver.find_element(By.ID, "seo-root")
        # print(element.text)

        # element = driver.find_element(By.CLASS_NAME, "qYMgrDY_H1477kqFiDOb")
        # print(element.text)

        element = driver.find_element(By.LINK_TEXT, "Hakkımızda")
        print(element.get_attribute("href"))
        element.click()
        driver.implicitly_wait(10)

        time.sleep(5)
    except Exception as e:
        print("Hata:",e)
    finally:
        print("Tarayıcı kapatıldı.")
        driver.quit()

selenium_test_2()
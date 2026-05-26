import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@allure.feature("Carian Google")
def test_google_search():
    # Buka pelayar web Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("1. Layari Google"):
            driver.get("https://google.com")
            time.sleep(1)

        with allure.step("2. Masukkan kata kunci carian"):
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys("Selenium Python")

        with allure.step("3. Tekan Enter"):
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)

        with allure.step("4. Semak tajuk halaman"):
            assert "Selenium" in driver.title

    except Exception as e:
        # Ambil gambar jika gagal
        allure.attach(driver.get_screenshot_as_png(), name="gagal", attachment_type=allure.attachment_type.PNG)
        raise e
    finally:
        driver.quit()

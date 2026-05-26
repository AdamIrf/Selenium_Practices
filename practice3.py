import time, random, json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

t = 2.5

options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")  # Blocks pop-up ads

#1. Launch browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

#2. Navigate to url 'http://automationexercise.com'
driver.get("http://automationexercise.com")
driver.maximize_window()
time.sleep(t)


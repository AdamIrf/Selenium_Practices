import time, random, json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

t = 2.5

#0 Import and assigned data from json to python variables
with open("practice2.json", "r") as file:
    user_data = json.load(file)

# Extract the credentials into variables
test_email = user_data["email"]
test_password = user_data["password"]

#1. Launch browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#2. Navigate to url 'http://automationexercise.com'
driver.get("http://automationexercise.com")
driver.maximize_window()
time.sleep(t)

#3. Verify that home page is visible successfully
assert "Automation Exercise" in driver.title
print("Validation Succeed: Main Page Visible!")
time.sleep(t)

#4. Click on 'Signup / Login' button
driver.find_element(By.LINK_TEXT, "Signup / Login").click()
time.sleep(t)

#5. Verify 'Login to your account' is visible
login_to_account = driver.find_element(By.XPATH, "//h2[contains(text(), 'Login to your account')]")
assert login_to_account.is_displayed()
print("Validation Succeed: 'Login to your account!' is visible")
time.sleep(t)

#6. Enter correct email address and password
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(test_email)
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys(test_password)

#7. Click 'login' button
driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
print("Success Login")
time.sleep(t)

#8. Verify that 'Logged in as username' is visible
# There is advertisement so we need to close it then bot can detect the 'Logged in as'
logged_in_as_username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[contains(., 'Logged in as')]"))
)

assert logged_in_as_username.is_displayed()
print("Validation Succeed: Logged in as username is visible!")
time.sleep(t)

#9. Click 'Delete Account' button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Delete Account')]"))).click()
print("Validation Succeed: Delete Account is clicked!")

#10. Verify that 'ACCOUNT DELETED!' is visible
assert driver.find_element(By.XPATH, "//b[contains(text(), 'Account Deleted!')]").is_displayed()
print("Validation Succeed: Account Deleted Page!")

#11. Click continue button
driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
print("Validation Succeed: Continue button is clicked")


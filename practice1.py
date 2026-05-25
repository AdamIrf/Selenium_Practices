import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

email = "emailanda22@gmail.com"
t = 1

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

#5. Verify 'New User Signup!' is visible
signup_text = driver.find_element(By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
assert signup_text.is_displayed()
print("Validation Succeed: 'New User Signup!' is visible")
time.sleep(t)

#6. Enter name and email address
driver.find_element(By.NAME, "name").send_keys("Adam Irfan")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email) #each automation test need to change email because one new got rejected
print("Validation Succeed: name and email address")
time.sleep(t)

#7. Click 'Signup' button
driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
print("Validation Succeed: Signup button is clicked")
time.sleep(t)

#8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
account_information = driver.find_element(By.XPATH, "//b[contains(text(), 'Enter Account Information')]")
assert account_information.is_displayed()
print("Validation Succeed: EAI is visibled")
time.sleep(t)

#9. Fill details: Title, Name, Email, Password, Date of birth
# A. Select Mr by check inspect Id button
driver.find_element(By.ID, "id_gender1").click()
time.sleep(t)

# B. Enter Password
driver.find_element(By.ID, "password").send_keys("KataLaluanAnda123")
time.sleep(t)

# C. Select Date of Birth using dropdown list
from selenium.webdriver.support.ui import Select

# Day
Select(driver.find_element(By.ID, "days")).select_by_value("15")
time.sleep(t)

# Month
Select(driver.find_element(By.ID, "months")).select_by_value("5")
time.sleep(t)

# Year
Select(driver.find_element(By.ID, "years")).select_by_value("2000")
time.sleep(t)

print("Validation Succeed: Main form filled!")
time.sleep(t)

#10. Select checkbox 'Sign up for our newsletter!'
driver.find_element(By.ID, "newsletter").click()
print("Validation Succeed: Checkbox clicked!")
time.sleep(t)

driver.find_element(By.ID, "optin").click()
print("Validation Succeed: Receive special offers clicked!")
time.sleep(t)

#11. Select checkbox 'Receive special offers from our partners!'

#12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number

#13. Click 'Create Account button'

#14. Verify that 'ACCOUNT CREATED!' is visible

#15. Click 'Continue' button

#16. Verify that 'Logged in as username' is visible

#17. Click 'Delete Account' button

#18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
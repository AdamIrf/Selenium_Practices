import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

random_email = f"adam_user{random.randint(1, 9999)}@gmail.com"
t = 2

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
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(random_email) #each automation test need to change email because one new got rejected
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

#11. Select checkbox 'Receive special offers from our partners!'
driver.find_element(By.ID, "optin").click()
print("Validation Succeed: Receive special offers clicked!")
time.sleep(t)

#12. Fill details: 
# First name
driver.find_element(By.ID, "first_name").send_keys("Muhamad Adam Irfan")
print("Validation Succeed: First Name filled")
time.sleep(t)

# Last name 
driver.find_element(By.ID, "last_name").send_keys("Mohd Nizam")
print("Validation Succeed: Last Name filled")
time.sleep(t)

# Company 
driver.find_element(By.ID, "company").send_keys("Coreium Sdn Bhd")
time.sleep(t)

# Address 
driver.find_element(By.ID, "address1").send_keys("Taman Maju")
time.sleep(t)

# Address2 
driver.find_element(By.ID, "address2").send_keys("Seri Iskandar")
time.sleep(t)

# Country 
Select(driver.find_element(By.ID, "country")).select_by_value("Singapore")
time.sleep(t)

# State
driver.find_element(By.ID, "state").send_keys("Perak")
time.sleep(t)

# City 
driver.find_element(By.ID, "city").send_keys("Entahla")
time.sleep(t)

# Zipcode 
driver.find_element(By.ID, "zipcode").send_keys("32610")
time.sleep(t)

# Mobile Number random

# a. Initial mobile code in Malaysia
prefixes = ["011", "012", "013", "014", "016", "017", "018", "019"]
random_prefix = random.choice(prefixes)

# b. Generate remaining 7 numbers 
# if 011 then the remaining numbers is 8 digit meanwhile then rest 7 digits
if random_prefix == "011":
    remaining_digits = str(random.randint(10000000, 99999999))  # 8 digits
else:
    remaining_digits = str(random.randint(1000000, 9999999))    # 7 digits

# c. Combine both
random_phone = random_prefix + remaining_digits

driver.find_element(By.ID, "mobile_number").send_keys(random_phone)
print("Validation Succeed: Mobile Number filled")
time.sleep(t)

#13. Click 'Create Account button'
driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()
print("Validation Succeed: Create Account is clicked")
time.sleep(t)

#14. Verify that 'ACCOUNT CREATED!' is visible
account_created = driver.find_element(By.XPATH, "//b[contains(text(), 'Account Created!')]")
assert account_created.is_displayed()
print("Validation Succeed: Arrived Account Created Page!")
time.sleep(t)

#15. Click 'Continue' button

#16. Verify that 'Logged in as username' is visible

#17. Click 'Delete Account' button

#18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
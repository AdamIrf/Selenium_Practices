# 🚀 Selenium Automation Testing Practices

This repository contains automated test scripts developed using **Selenium WebDriver (Python)** for the [Automation Exercise](https://automationexercise.com) website.

## 📋 Features & Test Cases Covered
* **User Registration Flow**: Automates the complete user signup process (Steps 1 to 21) using dynamic and randomized data generation.
* **Random Data Generation**: Implements random logic for generating unique emails, dates of birth, and Malaysian phone numbers to prevent duplicate errors.
* **Smart Synchronization**: Uses explicit waits (`WebDriverWait`) to handle asynchronous loading and dynamic elements smoothly.

## 🛠️ Prerequisites & Tech Stack
* **Language**: Python 
* **Framework**: Selenium 4
* **Browser**: Google Chrome & ChromeDriver

## 💻 How to Run the Script
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the project folder:
   ```bash
   cd Selenium_Practices
   ```
3. Run the registration test script:
   ```bash
   python practice1.py
   ```

## 📝 Future Enhancements
* Add advertisement blocker to ensure the smoothness of test process.
* Implement the **Page Object Model (POM)** design pattern to separate locators from test logic.
* Integrate **PyTest** framework for advanced test reporting and assertions.
* Add automated screenshot capture for failed test steps.

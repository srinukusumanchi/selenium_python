# Selenium Python Automation Framework
# selenium_python

A sample Selenium automation framework in Python using the Page Object Model, Pytest, and various utilities for effective UI testing.  
This framework is designed for automated testing of the [nopCommerce admin demo site](https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F).

---

## 📦 Folder Structure

```
selenium_python/
│
├── PageObject/         # Page Object classes (Python package)
├── testCases/          # Test classes (Python package)
├── utilities/          # Utility classes (Python package)
├── testdata/           # Test data files (Excel, CSV, etc.)
├── configuration/      # Config files (config.ini, etc.)
├── logs/               # Log files
├── screenshots/        # Test failure screenshots
├── reports/            # Test execution reports (HTML, Allure, etc.)
└── run.bat             # Batch file to run tests
```

---

## 🛠️ Installation

1. **Open PyCharm**  
   Go to *Settings → Project → Python Interpreter*.

2. **Install the following libraries:**
   - `selenium`
   - `pytest`
   - `pytest-html`
   - `pytest-xdist`
   - `openpyxl`
   - `allure-pytest`

   ```
   pip install selenium pytest pytest-html pytest-xdist openpyxl allure-pytest
   ```

---

## 🔑 Application Under Test

- **URL:** [nopCommerce Admin Login](https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F)
- **Credentials:**
  - Email: `admin@yourstore.com`
  - Password: `admin`

---

## 🧩 Page Object Structure

- **Element Locators:**  
  Define page elements at the top of each Page Object class.  
  Example:
  ```python
  textbox_username_id = "Email"
  ```

- **Action Methods:**  
  Define interaction methods for each page.  
  Example:
  ```python
  def setUserName(self, userName):
      self.driver.find_element(By.ID, self.textbox_username_id).clear()
      self.driver.find_element(By.ID, self.textbox_username_id).send_keys(userName)
  ```

---

## 📝 Writing Test Cases

- **Naming Convention:**
  - Test class name: `test_*.py` or `*_test.py`
  - Test method name: `test_*` or `*_test`

- **Sample Test Case:**

  ```python
  def test_login(self, setup):
      self.driver = setup
      self.driver.get(self.baseURL)

      self.loginPage = LoginPage(self.driver)
      self.loginPage.setUserName(self.username)
      self.loginPage.setPassword(self.password)
      self.loginPage.clickLogin()
      actualTitle = self.driver.title

      if actualTitle == "Dashboard / nopCommerce administration":
          assert True
          self.driver.close()
      else:
          self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
          self.driver.close()
          assert False
  ```

---

## ⚙️ Fixtures (in `testCases/conftest.py`)

Reusable setup/teardown code can be placed in fixtures:

```python
import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
```

- Use the `setup` fixture in your test methods for driver initialization.

---

## 📸 Screenshots

- To capture a screenshot on failure or for debugging:

  ```python
  self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
  ```





This project provides a robust, reusable, and easy-to-understand automation framework for web application testing using Selenium, Pytest, and the Page Object Model (POM) design pattern. The framework is designed to test the login functionality of the nopCommerce admin portal.

## 1. Prerequisites

### Installation via PyCharm

To get started, you'll need to install the necessary Python packages.

1.  Open your PyCharm IDE.
2.  Navigate to **`Settings`** (or **`Preferences`** on macOS).
3.  Go to **`Project: [Your Project Name]`** → **`Python Interpreter`**.
4.  Click the `+` button to add new packages.
5.  Search for and install the following libraries:
    -   `selenium`: The core library for browser automation.
    -   `pytest`: A powerful and easy-to-use testing framework for Python.
    -   `pytest-html`: For generating detailed, shareable HTML test reports.
    -   `pytest-xdist`: To enable parallel test execution, speeding up your test runs.
    -   `openpyxl`: For handling test data from Excel files.
    -   `allure-pytest`: For generating comprehensive and interactive Allure test reports.

## 2. Project Structure

The project is organized using the Page Object Model (POM) to ensure maintainability, reusability, and readability.

/YourProjectName
├── PageObjects/ # Stores all Page Object classes for each web page.
│ └── LoginPage.py # Example Page Object for the Login page.
├── testCases/ # Contains all test scripts and test suites.
│ ├── conftest.py # Defines Pytest fixtures for reusable components like the WebDriver setup.
│ └── test_login.py # Example test script for login functionality.
├── utilities/ # Holds helper functions, reusable methods, and configuration readers.
├── testdata/ # Stores data files used in tests, such as Excel files.
├── configuration/ # Contains configuration files for the project (e.g., INI or JSON).
├── logs/ # Directory for storing test execution logs.
├── screenshots/ # Location where screenshots are saved on test failure.
├── reports/ # Stores generated test reports (e.g., HTML, Allure).
└── run.bat # A simple batch file to execute tests from the command line on Windows.

from PageObjects.LoginPage import LoginPage

class TestLogin:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()

        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            assert False
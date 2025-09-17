import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actualTitle = self.driver.title

        if (actualTitle == "nopCommerce demo store. Login"):
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actualTitle = self.driver.title
        if actualTitle == "Dashboard / nopCommerce administration":
            assert  True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False


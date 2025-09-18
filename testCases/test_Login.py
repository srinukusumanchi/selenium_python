from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()
    def test_homePageTitle(self, setup):
        self.logger.info(" **********Test_001_Login************ ")
        self.logger.info(" **********Verifying Home Page Title************ ")
        self.driver = setup
        self.driver.get(self.baseURL)
        actualTitle = self.driver.title

        if (actualTitle == "nopCommerce demo store. Login"):
            assert True
            self.driver.close()
            self.logger.info(" ********** Home Page Title is passed************ ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error(" ********** Home Page Title is failed************ ")
            assert False

    def test_login(self, setup):
        self.logger.info(" ********** Verifying Login Test************ ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actualTitle = self.driver.title
        if actualTitle == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info(" ********** Login Test is passed************ ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error(" ********** Login Test is failed************ ")
            assert False

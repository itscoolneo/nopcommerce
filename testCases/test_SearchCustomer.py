import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import searchCustomer
from selenium.webdriver.common.by import By


class Test_004_searchCustomer:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchCustomer(self, setup):
        self.logger.info("****** Test_004_searchCustomer ******")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfull ******")

        self.logger.info("****** Search Customer By Email Test Started ******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.sercust = searchCustomer(self.driver)
        self.sercust.setEmail("victoria_victoria@nopCommerce.com")
        self.sercust.clickSearchButton()
        time.sleep(3)
        # status = sercust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        # if status== True:
        #     assert True
        #     self.logger.info("****** Search Result Test Passed ******")
        # else:
        #     assert False
        #
        # self.driver.close()

        self.serchResult = self.driver.find_element(By.XPATH, "//div//td[2]").text
        print(self.serchResult)

        # self.resultNotfound=self.driver.find_element(By.XPATH,"//td[@class='dataTables_empty']").text
        if self.driver.find_element(By.XPATH, "//div//td[2]").is_displayed():
            if "victoria_victoria@nopCommerce.com" in self.serchResult:
                self.logger.info("****** Search Result Test Passed ******")
                self.driver.close()
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_searchCustomer.png")
                self.logger.error("****** Search Result Test Failed")
                self.driver.close()
                assert False

        else:
            self.logger.info("****** Element not visible issue ******")
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchByFirstName(self, setup):
        self.logger.info("****** test_searchByFirstName ******")
        self.driver = setup
        self.driver.implicitly_wait(60)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.set_script_timeout(2)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfull ******")

        self.logger.info("****** Search Customer By First name test started ******")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.sercust = searchCustomer(self.driver)
        self.sercust.setFname("Victoria")
        self.sercust.clickSearchButton()
        self.serchResult = self.driver.find_element(By.XPATH, "//div//td[2]").text
        if self.driver.find_element(By.XPATH,"//div//td[2]").is_displayed():
            if "victoria_victoria@nopCommerce.com" in self.serchResult:
                self.logger.info("****** Search by first name test passed ******")
                assert True
                self.driver.close()
            else:
                self.logger.error("****** Search by first name test failed ******")
                self.driver.close()
                assert False

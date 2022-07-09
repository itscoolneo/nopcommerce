import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("****** TEST_003_ADDCUSTOMER ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Successfull ******")

        self.logger.info("****** Starting Add Customer Test ******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("****** Providing customer info ******")

        self.email = random_generator() + "@gmail.com"
        # self.email = "testmybcode88@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCutomerRole("Guest")
        self.addcust.setManagerOfVendors("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstname("Dharmesh")
        self.addcust.setLastname("Soni")
        self.addcust.setCompanyname("D & D Company")
        self.addcust.setAdmincontent("This is for content")
        self.addcust.clickOnSave()

        self.logger.info("****** Saving Customer Info ******")

        self.logger.info("****** Add Customer Validation Started ******")

        self.msg = self.driver.find_element(By.TAG_NAME, ("body")).text
        print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("****** Add Customer Test Passed ******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("****** Add Customer Test Failed ******")
            assert False
        self.logger.info("****** ENDING HOME PAGE TITILE TEST")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

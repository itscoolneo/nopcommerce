import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import logging


class Test_001_Login:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*****Test_001_Login*****")
        self.logger.info("*****Verifying Title*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_titile = self.driver.title
        if act_titile == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****Home page title passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*****Home page title failed*****")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*****Verifying Login Test*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_titile = self.driver.title

        if act_titile == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****Login Test Passed*****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*****Login Test Failed*****")
            assert False

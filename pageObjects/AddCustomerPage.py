import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium


# ADD CUSTOMER PAGE

class AddCustomer:
    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    RdMaleGender_id = "Gender_Male"
    RdFemaleGender_id = "Gender_Female"
    txtDateOfBirth_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    cb_itx_xpath = "//input[@id='IsTaxExempt']"
    lstCustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    lstItemAdministrators_xpath = "//li[normalize-space()='Administrators']"
    lstItemGuest_xpath = "//li[normalize-space()='Guests']"
    lstItemRegistered_xpath = "//li[@id='60334198-0ab0-45b5-b62a-952d3e692b0d']"
    lstItemVendor_xpath = "//li[contains(text(),'Vendors')]"
    drpMngrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btn_Save_xpath = "//button[@name='save']//i[@class='far fa-save']"



    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCutomerRole(self, role):
        self.driver.find_element(By.XPATH, self.lstCustomerRoles_xpath).click()
        time.sleep(2)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemAdministrators_xpath)
        elif role == "Guest":
            time.sleep(2)
            self.listitem = self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemGuest_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemGuest_xpath)
        time.sleep(2)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendors(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpMngrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.RdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.RdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.RdMaleGender_id).click()

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstname_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lastname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDateOfBirth_xpath).send_keys(dob)

    def setCompanyname(self, cname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(cname)

    def setAdmincontent(self, admincontent):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(admincontent)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()

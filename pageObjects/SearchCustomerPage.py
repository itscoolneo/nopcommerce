from selenium.webdriver.common.by import By


class searchCustomer:
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstName_xpath = "//input[@id='SearchFirstName']"
    txtLastName = "//input[@id='SearchLastName']"
    btn_Search_xpath = "//button[@id='search-customers']"
    tblSearchResult_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tblRows_xpath = "//table[@id='customers-grid']//tr"
    tblColumn_xpath = "//table[@id='customers-grid']//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setFname(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLname(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName).send_keys(lname)

    def clickSearchButton(self):
        self.driver.find_element(By.XPATH, self.btn_Search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tblRows_xpath))

    def getNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH, self.tblColumn_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']//tr[" + str(r) + "]/td")
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']//tr[" + str(r) + "]/td")
            if name == Name:
               flag = True
               break
            return flag

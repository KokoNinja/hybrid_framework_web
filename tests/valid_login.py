import time
import pytest
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from assertpy import assert_that
from selenium.webdriver.support.select import Select
from utilities import data_source

class TestAdd_HR(WebDriverWrapper):
    #To verify the valid record of add employee without providing credentials
    @pytest.mark.parametrize("firstname,lastname,email,title,company,phone,emp_value,country",data_source.test_valid_login)

    def test_add_valid_emp(self,firstname,lastname,email,title,company,phone,emp_value,country):
        self.driver.find_element(By.LINK_TEXT,"Try it free").click()
        self.driver.find_element(By.ID,"FirstName").send_keys(firstname)
        self.driver.find_element(By.ID,"LastName").send_keys(lastname)
        self.driver.find_element(By.ID,"Email").send_keys(email)
        self.driver.find_element(By.ID,"Title").send_keys(title)
        self.driver.find_element(By.ID,"Company").send_keys(company)
        self.driver.find_element(By.ID,"Phone").send_keys(phone)
        select_count = Select(self.driver.find_element(By.ID, "Employees_Text__c"))
        select_count.select_by_value(emp_value)
        select_country = Select(self.driver.find_element(By.ID, "Country"))
        select_country.select_by_value(country)
        self.driver.implicitly_wait(30)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Get Free Trial']").click()
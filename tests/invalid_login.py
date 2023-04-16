import time
import pytest
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from assertpy import assert_that
from selenium.webdriver.support.select import Select
from utilities import data_source

class TestAddEmployee(WebDriverWrapper):

    def test_invalid_employee(self):
        self.driver.find_element(By.LINK_TEXT,"Log In").click()
        self.driver.find_element(By.XPATH, "//input[@id='domain']").send_keys("einfochips")
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        actual_error=self.driver.find_element(By.XPATH,"//span[@class='hI9SEurDvDymAAD3fEZKBA==']").text
        assert_that("That doesn't look like").contains(actual_error)

    @pytest.mark.parametrize("domain, expected_error",data_source.test_invalid_login_data)
    def test_invalid_login(self,domain,expected_error):
        self.driver.find_element(By.LINK_TEXT, "Log In").click()
        self.driver.find_element(By.XPATH, "//input[@id='domain']").send_keys(domain)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        actual_error = self.driver.find_element(By.XPATH, "//span[@class='hI9SEurDvDymAAD3fEZKBA==']").text
        assert_that(expected_error).contains(actual_error)
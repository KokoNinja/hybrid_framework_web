import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriverWrapper:
    driver=None
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name=""

        if browser_name=="edge":
            self.driver=webdriver.Edge()
        elif browser_name=="ff":
            self.driver==webdriver.Firefox()
        else:
            self.driver=webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.bamboohr.com")
        yield
        self.driver.quit()


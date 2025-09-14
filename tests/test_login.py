import pytest
from pages.login_page import LoginPage
from utils.config_reader import read_config
from utils.getWaits import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.mark.dependency(name="login")
    def test_login_user(self,driver):
        try:
            getContent = read_config()
            BaseURL = getContent['base_url']
            driver.get(BaseURL)
            print("Page URL:", driver.current_url)
            print("Page Title:", driver.title)
            loginPage = LoginPage(driver) 
            loginPage.login(getContent['username'],getContent['password'])
            assert "CEP" in driver.title

        except Exception as e:
            print(f"{e}")
            raise

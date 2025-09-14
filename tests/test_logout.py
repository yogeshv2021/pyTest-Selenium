from selenium.webdriver.common.by import By
from utils.getWaits import Waits
from pages.login_locaters import Locators
from selenium.common.exceptions import TimeoutException
import pytest


@pytest.mark.usefixtures("driver")
class TestLogout:

    @pytest.mark.dependency(depends=["login"])
    def testlogout(self,driver):
        loc = Locators(driver)
        loc.Logout()

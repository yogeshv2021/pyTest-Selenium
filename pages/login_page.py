from selenium.webdriver.common.by import By
from utils.getWaits import Waits
from pages.login_locaters import Locators

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        try:
            Waits.checkExplicitWaits(self.driver,Locators.LOGIN_BTN,"Presence",5)
            self.driver.find_element(*Locators.LOGIN_BTN).click()
            self.driver.find_element(*Locators.USERNAME).send_keys(username)
            self.driver.find_element(*Locators.PASSWORD).send_keys(password)
            self.driver.find_element(*Locators.SUBMIT_BTN).click()

        except Exception as e:
            print(f"error occured.{e}")
            raise

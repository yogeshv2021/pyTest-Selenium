from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.getWaits import Waits




class Locators:
    LOGIN_BTN = (By.XPATH,"//*[text()='Login']")
    USERNAME = (By.XPATH,"//*[@id='username']")
    PASSWORD = (By.XPATH,"//*[@name='password']")
    SUBMIT_BTN = (By.XPATH,"//*[@type='submit']")
    LOGOUT_IMGBTN = (By.XPATH,"//img[contains(@id,'LogOut')]")
    LOGOUT_BTN = (By.XPATH,"//*[text()='Logout']")

    def __init__(self,driver):
        self.driver = driver

    def Logout(self):
       try:
           Waits.checkExplicitWaits(self.driver,Locators.LOGOUT_IMGBTN,"Visible")
           self.driver.find_element(*Locators.LOGOUT_IMGBTN).click()
           self.driver.find_element(*Locators.LOGOUT_BTN).click()

       except TimeoutException as e:
           print(f"Error.{e}")
           raise

       except Exception as e:
           self.driver.execute_script("arguments[0].click;",self.LOGOUT_IMGBTN)
           print(f"Error.{e}")
           raise


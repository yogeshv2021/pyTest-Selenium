from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Waits:

    @staticmethod
    def checkExplicitWaits(driver,locator,type,Timeout=10,Text="Dashboard",getIcon="icon"):

        wait = WebDriverWait(driver,Timeout)

        print(locator)

        if type=="title":
            wait.until(EC.title_contains(Text))

        elif type=="Presence":
            wait.until(EC.presence_of_element_located(locator))

        elif type=="Visible":
            wait.until(EC.visibility_of_element_located(locator))

        elif type=="Text":
            wait.until(EC.text_to_be_present_in_element(locator,Text))

        elif type=="Click":
            icon = wait.until(EC.element_to_be_clickable(locator))
            return icon

        elif type=="Alert":
            wait.until(EC.alert_is_present())

        elif type=="Expanded":
            wait.until(lambda d: getIcon.get_attribute("aria-expanded") == "true")

        else:
            raise ValueError(f"Unsupported wait type: {type}")

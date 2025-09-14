from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException,ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
from time import sleep
from utils.getWaits import Waits
import os
import pytest

@pytest.mark.usefixtures("driver")
class Locators:

    SIDE_BAR = (By.XPATH,"//*[@class='btn btn-outline btn-sm']//i")
    MENU_CLICK = (By.XPATH,"//*[normalize-space(text())='VOICE']")
    AUDIO_MANAGER_MENU = (By.XPATH,"//*[normalize-space(text())='Audio Manager']")
    ADD_SOUND_FILE = (By.XPATH,"//button[text()='Add new sound file']")
    FILE_TYPE = (By.XPATH,"//*[@formcontrolname='fileType']")
    ENTER_TITLE = (By.XPATH,"//*[@placeholder='Title']")
    UPLOAD_FILE = (By.XPATH,"//*[@id='txtFileUpload']")
    SELECT_TAGS = (By.XPATH,"//*[@fieldname='selectTag' and @type='text']")	
    SAVE_BUTTON = (By.XPATH,"//*[text()='Save']")
    POPUP_ALERT = (By.XPATH,"//*[@id='toast-container']//preceding-sibling::div")
    FILE_NAME = r"/home/yoge1542/Automation/RagAsTesting/selenium/Upload/IVRS.mp3"
    PopupText = "Internal Server Error"
    TAG = "T1"

    SEARCH_TEXT=  (By.XPATH,"//*[@placeholder='Search for a Sound']")
    VOICE_TEXT = "IVRSNEW"
    VOICE_TAG_TEXT = "IVRSTAG"
    VOICE_CLICK_ICON = (By.XPATH,"//mat-icon[normalize-space(text())='more_vert']")
    VOICE_EDIT_ICON = (By.XPATH,"//*[contains(@class,'mat-ripple mat-menu-ripple')]")
    VOICE_EDIT_FILE_NAME = (By.XPATH,"//*[@placeholder='File Name']")
    VOICE_EDIT_SELECT_TAGS = (By.XPATH,"//*[contains(@class,'col-sm-12 mt-2') ]//*[@placeholder='Select tags']")
    VOICE_CLOSE_BUTTON_ADD = (By.XPATH,"//*[contains(@class,'modal-content')]//*[@type='button' and text()='Close']")
    VOICE_CLOSE_BUTTON_EDIT = (By.XPATH,"//*[contains(@id,'updatemymodel')]//*[@type='button' and text()='Close']")
    VOICE_UPDATE_BUTTON = (By.XPATH,"//*[@type='button' and text()='Update']")

    def __init__(self,driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def getElement(self):
        Waits.checkExplicitWaits(self.driver,Locators.SIDE_BAR,"Visible")
        self.driver.find_element(*Locators.SIDE_BAR).click()
        Waits.checkExplicitWaits(self.driver,Locators.MENU_CLICK,"Visible")
        self.driver.find_element(*Locators.MENU_CLICK).click()

    def MenuElement(self):
        try:
           Waits.checkExplicitWaits(self.driver,Locators.AUDIO_MANAGER_MENU,"Click")
           self.driver.find_element(*Locators.AUDIO_MANAGER_MENU).click()
        except StaleElementReferenceException as error:
           self.getDynamicElements()
           
        except Exception as e:
           print(f"error {e}")
           raise


    def SoundElement(self):
        getElement=self.driver.find_elements(*Locators.ADD_SOUND_FILE)
        for idx,element in enumerate(getElement):
            if idx==1:
                element.click()

    def SelectFileType(self):
        Waits.checkExplicitWaits(self.driver,Locators.FILE_TYPE,"Visible")
        element = self.driver.find_element(*Locators.FILE_TYPE)
        dropdown = Select(element)
        dropdown.select_by_value('IVR')

    def EnterTitle(self):
        Waits.checkExplicitWaits(self.driver,Locators.ENTER_TITLE,"Visible")
        title = self.driver.find_element(*Locators.ENTER_TITLE)
        title.send_keys("FileUploadofIVR")

    def UploadFile(self):
        FileUpload = self.driver.find_element(*Locators.UPLOAD_FILE)
        self.driver.execute_script("arguments[0].style.display='block';",FileUpload)
        path = os.path.exists(self.FILE_NAME)
        assert path
        if path:
            FileUpload.send_keys(self.FILE_NAME)

    def SelectTags(self):
        Tags = self.driver.find_elements(*Locators.SELECT_TAGS)
        for idx,element in enumerate(Tags):
            if idx==0:
                element.send_keys(self.TAG)

    def SaveButton(self):
        Button = self.driver.find_element(*Locators.SAVE_BUTTON)
        Button.click()

    def CheckAlert(self):
        try:
           Waits.checkExplicitWaits(self.driver,Locators.POPUP_ALERT,"Text",10,self.PopupText)
           getAlert = self.driver.find_element(*Locators.POPUP_ALERT)

        except Exception as e:
           print(f"error {e}")
           raise
        
    def SearchElement(self):
        try:
           Text = self.driver.find_element(*Locators.SEARCH_TEXT)
           Text.send_keys(Locators.VOICE_TEXT)

        except Exception as e:
           print(f"error {e}")
           raise

    def clickIcon(self):

        for idx in range(3):
            try:
                icon = Waits.checkExplicitWaits(self.driver,Locators.VOICE_CLICK_ICON,"Click")
                VoiceClick = self.driver.find_element(*Locators.VOICE_CLICK_ICON)
                self.driver.execute_script("arguments[0].scrollIntoView(true);",VoiceClick )
                self.driver.execute_script("arguments[0].click();",VoiceClick)
                icon = Waits.checkExplicitWaits(self.driver,Locators.VOICE_CLICK_ICON,"Expanded",10,"",icon)

                return True

            except ElementClickInterceptedException as error:
                continue

            except StaleElementReferenceException as error:
                continue
           
            except Exception as e:
                print(f"error {e}")
                raise



    def editIcon(self,getId):
        try:
           Waits.checkExplicitWaits(self.driver,Locators.VOICE_EDIT_ICON,"Visible")
           editClick = self.driver.find_elements(*Locators.VOICE_EDIT_ICON)
           for idx,getElement in enumerate(editClick):
               if idx==getId:
                   self.driver.execute_script("arguments[0].scrollIntoView(true);",getElement )
                   self.driver.execute_script("arguments[0].click();",getElement)

        except StaleElementReferenceException as error:
           self.getDynamicElements(*Locators.VOICE_EDIT_ICON)
           
        except Exception as e:
           print(f"error {e}")
           raise


    def editFileName(self):
        try:
           Waits.checkExplicitWaits(self.driver,Locators.VOICE_EDIT_FILE_NAME,"Visible")
           EditFilename = self.driver.find_element(*Locators.VOICE_EDIT_FILE_NAME)
           self.driver.execute_script("arguments[0].scrollIntoView(true);",EditFilename)
           EditFilename.clear()
           EditFilename.send_keys(Locators.VOICE_TEXT)


        except Exception as e:
           print(f"error {e}")
           raise


    def editTags(self):
        try:
           Waits.checkExplicitWaits(self.driver,Locators.VOICE_EDIT_SELECT_TAGS,"Visible")
           EditTags= self.driver.find_element(*Locators.VOICE_EDIT_SELECT_TAGS)
           self.driver.execute_script("arguments[0].scrollIntoView(true);",EditTags)
           EditTags.clear()
           EditTags.send_keys(Locators.VOICE_TAG_TEXT)

        except Exception as e:
           print(f"error {e}")
           raise


    def CloseButtonAdd(self,ElementId):
        try:
           Waits.checkExplicitWaits(self.driver,Locators.VOICE_CLOSE_BUTTON_ADD,"Click")
           CloseClick = self.driver.find_elements(*Locators.VOICE_CLOSE_BUTTON_ADD)
           for idx,getElement in enumerate(CloseClick):
               if idx==ElementId:
                   self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",getElement )
                   self.driver.execute_script("arguments[0].click();",getElement )
           sleep(5)

        except Exception as e:
           print(f"error {e}")
           raise


    def CloseButtonEdit(self):
        try:
           Waits.checkExplicitWaits(self.driver,Locators.VOICE_CLOSE_BUTTON_EDIT,"Click")
           CloseClick = self.driver.find_element(*Locators.VOICE_CLOSE_BUTTON_EDIT)
           self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",CloseClick )
           self.driver.execute_script("arguments[0].click();",CloseClick )
           sleep(5)

        except Exception as e:
           print(f"error {e}")
           raise

    def UpdateButton(self):
        try:
           updateClick = self.driver.find_element(*Locators.VOICE_UPDATE_BUTTON)
           self.driver.execute_script("arguments[0].click();",updateClick)
           sleep(5)

        except Exception as e:
           print(f"error {e}")
           raise

    def getDynamicElements(self,*args):
        start=0
        end=3
        while start<end:
           try:
              self.driver.find_element(args[0],args[1]).click()
           except Exception as e:
              start=start+1

         

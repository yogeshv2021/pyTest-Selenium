from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException,ElementClickInterceptedException,NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep
from utils.getWaits import Waits
import os
import pytest

@pytest.mark.usefixtures("driver")
class FlowBuilderLocators:

    SIDE_BAR = (By.XPATH,"//*[@class='btn btn-outline btn-sm']//i")
    RIGHT_SIDE_BAR= (By.XPATH,"//*[@class='bi bi-chevron-double-right']")
    LEFT_SIDE_BAR = (By.XPATH,"//*[@class='bi bi-chevron-double-left']")

    RECEIVE_INPUT = (By.XPATH,"//*[text()='Receive Input']/following-sibling::span")
    TARGET_ELEMENT =  (By.XPATH,"//*[contains(@class,'react-flow__edgelabel-renderer')]//following-sibling::div")
    MENU_CLICK = (By.XPATH,"//*[normalize-space(text())='FLOW BUILDER']")
    FLOW_NAME = (By.XPATH,"//mat-cell//*[normalize-space(text())='ChatQueryCall']")
    SYSTEM_FAIL = (By.XPATH,"//*[contains(@class,'node-receiveInput')]//*[contains(@data-handleid,'system_fail')]")
    FLOW_CONNECT = (By.XPATH,"//*[contains(@class,'react-flow__nodes')]//*[contains(@class,'react-flow__node react-flow__node-')]//*[contains(@data-handleid,'Source_receiveInput')]")

    def __init__(self,driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def getflowBuilderElement(self):
        try:
            self.Element = self.driver.find_element(*FlowBuilderLocators.LEFT_SIDE_BAR)
            if self.Element:
                Waits.checkExplicitWaits(self.driver,FlowBuilderLocators.MENU_CLICK,"Visible")
                self.driver.find_element(*FlowBuilderLocators.MENU_CLICK).click()
            sleep(10)

        except NoSuchElementException as exception:
            self.Element = self.driver.find_element(*FlowBuilderLocators.RIGHT_SIDE_BAR)
            if self.Element:
                Waits.checkExplicitWaits(self.driver,FlowBuilderLocators.SIDE_BAR,"Visible")
                self.driver.find_element(*FlowBuilderLocators.SIDE_BAR).click()

                Waits.checkExplicitWaits(self.driver,FlowBuilderLocators.MENU_CLICK,"Visible")
                self.driver.find_element(*FlowBuilderLocators.MENU_CLICK).click()
            sleep(10)


    def getFlowName(self):
        try:

           Waits.checkExplicitWaits(self.driver,FlowBuilderLocators.FLOW_NAME,"Click")

           Element = self.driver.find_element(*FlowBuilderLocators.FLOW_NAME)
           Element.click()

           Waits.checkExplicitWaits(self.driver,FlowBuilderLocators.RECEIVE_INPUT,"Visible")
           Waits.checkExplicitWaits(self.driver,FlowBuilderLocators.TARGET_ELEMENT,"Visible")

           source= self.driver.find_element(*FlowBuilderLocators.RECEIVE_INPUT)
           target = self.driver.find_element(*FlowBuilderLocators.TARGET_ELEMENT)

           self.driver.execute_script("arguments[0].setAttribute('draggable', 'true');", source)
           self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
 
           self.actions.click_and_hold(source).move_to_element_with_offset(target,40,30).release().perform()
           self.driver.execute_script("""const evt = new MouseEvent('click', { bubbles: true, cancelable: true, view: window });arguments[0].dispatchEvent(evt);""", target)
           print("Drag and drop successful")

           sleep(10)
           Waits.checkExplicitWaits(self.driver,FlowBuilderLocators.FLOW_CONNECT,"Visible")

           systemFailConnect= self.driver.find_elements(*FlowBuilderLocators.SYSTEM_FAIL)
           ReceiveInputConnect= self.driver.find_elements(*FlowBuilderLocators.FLOW_CONNECT)

           for idx,connectelement in enumerate(systemFailConnect):
               if idx==0:
                   self.actions.click_and_hold(connectelement).move_to_element(ReceiveInputConnect[0]).release().perform()
                   print("Click-and-release completed")



        except StaleElementReferenceException as error:
           print("Stale element, retrying...")
           js_drag_drop="""
               const source = arguments[0];
               const target = arguments[1];
               const dataTransfer = new DataTransfer();
 
               source.dispatchEvent(new DragEvent('dragstart', {dataTransfer}));
               target.dispatchEvent(new DragEvent('drop', {dataTransfer}));
               source.dispatchEvent(new DragEvent('dragend', {dataTransfer}));
           """

           self.driver.execute_script(js_drag_drop,source,target)
           self.getDynamicElements(*FlowBuilderLocators.TARGET_ELEMENT,source)
           
        except Exception as e:
           print(f"error {e}")
           raise

    def getSleep(self):
        sleep(30)


        
    def getDynamicElements(self,*args,source):
        start=0
        end=3
        while start<end:
           try:
              target = self.driver.find_element(args[0],args[1])
              self.driver.execute_script("arguments[0].setAttribute('draggable', 'true');", source)
              self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
              self.actions.click_and_hold(source).move_to_element_with_offset(target,50,50).release().perform()
              print("Drag and drop successful")
              return True
           except Exception as e:
              start=start+1


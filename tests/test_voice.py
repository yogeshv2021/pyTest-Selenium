from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pages.voice_menu import Locators


@pytest.mark.usefixtures("driver")
class TestVoice:

    def test_voice_create(self,driver):

        loc = Locators(driver)

        loc.getElement()

        loc.MenuElement()

        loc.SoundElement()

        loc.SelectFileType()

        loc.EnterTitle()

        loc.UploadFile()

        loc.SelectTags()

        loc.SaveButton()
 
        loc.CheckAlert()

        loc.CloseButtonAdd(0)

    def test_voice_edit(self,driver):

        loc = Locators(driver)

        loc.MenuElement()

        loc.SearchElement()

        loc.clickIcon()

        loc.editIcon(0)

        loc.editFileName()

        loc.editTags()

        loc.UpdateButton()

        loc.CloseButtonEdit()


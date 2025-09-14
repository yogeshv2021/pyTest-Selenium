from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pages.flowbuilder_menu import FlowBuilderLocators


@pytest.mark.usefixtures("driver")
class TestFlowBuiler:

    def test_flow_view(self,driver):

        loc = FlowBuilderLocators(driver)

        loc.getflowBuilderElement()

        loc.getFlowName()

        loc.getSleep()

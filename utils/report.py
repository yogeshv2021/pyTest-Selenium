import allure

class report:

    def test_report(driver,report):
        report.screenshot("Before clicking button", target=driver)
        report.screenshot("After clicking button",target=driver)

    def allure_report(driver):
        allure.attachment(driver.get_screenshot_as_png(),name="Start",attachment_type=allure.attachment_type.PNG)
        allure.attachment(driver.get_screenshot_as_png(),name="After click",attachment_type=allure.attachment_type.PNG)

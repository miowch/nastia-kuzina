from typing import Final

from appium.webdriver.common.appiumby import AppiumBy

from Task2.utils.ui.main_page_object import MainPageObject


class WelcomePageObject (MainPageObject):
    image: Final = 'com.monefy.app.lite:id/imageViewHero'
    continueButton: Final = 'com.monefy.app.lite:id/buttonContinue'

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_image(self):
        return self.wait_for_element_present(
            by=(AppiumBy.ID, self.image),
            error_message='Cannot find imageViewHero'
        )

    def tap_continue(self):
        return self.wait_for_element_and_click(
            by=(AppiumBy.ID, self.continueButton),
            error_message='Cannot find buttonContinue'
        )
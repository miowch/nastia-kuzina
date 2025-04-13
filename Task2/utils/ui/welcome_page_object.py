from typing import Final

import allure

from Task2.utils.ui.main_page_object import MainPageObject


class WelcomePageObject (MainPageObject):
    image: Final = 'id:com.monefy.app.lite:id/imageViewHero'
    continueButton: Final = 'id:com.monefy.app.lite:id/buttonContinue'

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Wait for image")
    def wait_for_image(self):
        return self.wait_for_element_present(
            self.image,
            error_message='Cannot find imageViewHero'
        )

    @allure.step("Tap Continue")
    def tap_continue(self):
        return self.wait_for_element_and_click(
            self.continueButton,
            error_message='Cannot find buttonContinue'
        )
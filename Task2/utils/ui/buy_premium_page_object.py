from typing import Final

from Task2.utils.ui.main_page_object import MainPageObject


class BuyPremiumPageObject (MainPageObject):
    closeButton: Final = 'id:com.monefy.app.lite:id/buttonClose'

    def __init__(self, driver):
        super().__init__(driver)

    def close_screen(self):
        return self.wait_for_element_and_click(
            self.closeButton,
            error_message='Cannot find buttonClose'
        )
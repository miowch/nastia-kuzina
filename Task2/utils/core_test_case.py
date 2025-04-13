import unittest

from Task2.utils.ui.buy_premium_page_object import BuyPremiumPageObject
from Task2.utils.ui.main_page_object import MainPageObject
from Task2.utils.ui.welcome_page_object import WelcomePageObject

from Task2.utils.webdriver import Driver


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().driver
        self.main_page_object = MainPageObject(self.driver)
        self.welcome_page_object = WelcomePageObject(self.driver)
        self.buy_premium_page_object = BuyPremiumPageObject(self.driver)

        for welcome_step in range (4):
            self.welcome_page_object.wait_for_image()
            self.welcome_page_object.tap_continue()

        self.buy_premium_page_object.close_screen()

    def tearDown(self):
        if self.driver:
            self.driver.quit()
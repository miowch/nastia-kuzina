import unittest

from Task2.utils.ui.main_page_object import MainPageObject
from appium.webdriver.common.appiumby import AppiumBy

from Task2.utils.webdriver import Driver


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().driver
        self.main_page_object = MainPageObject(self.driver)
        self.main_page_object.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.main_page_object.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.main_page_object.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.main_page_object.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonClose'),
            error_message='Cannot find buttonClose'
        )

    def tearDown(self):
        if self.driver:
            self.driver.quit()
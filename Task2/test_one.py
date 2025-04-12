from appium.webdriver.common.appiumby import AppiumBy
from Task2.utils.core_test_case import CoreTestCase
from Task2.utils.ui.main_page_object import MainPageObject


class TestClass(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.main_page_object = MainPageObject(self.driver)

    def test_add_expenses(self):
        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/expense_button'),
            error_message='Cannot find expense_button'
        )
        self.main_page_object.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/amount_text'),
            error_message='Cannot find amount_text'
        )
        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonKeyboard5'),
            error_message='Cannot find buttonKeyboard5'
        )
        self.main_page_object.wait_for_element_and_send_keys(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewNote'),
            value='coffee',
            error_message='Cannot find textViewNote'
        )
        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/keyboard_action_button'),
            error_message='Cannot find keyboard_action_button'
        )
        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.monefy.app.lite:id/textCategoryName" and @text="Eating out"]'),
            error_message='Cannot find category Eating out'
        )

        self.main_page_object.assert_element_has_text(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/balance_amount'),
            expected_text='Balance -$5.00',
            error_message='Cannot find balance_amount'
        )

        self.main_page_object.wait_for_element_present(
            by=(AppiumBy.XPATH, '//android.widget.TextView[@text="100%"]'),
            error_message='Cannot find text 100%'
        )

        self.main_page_object.assert_element_has_text(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/expense_amount_text'),
            expected_text='$5.00',
            error_message='Cannot find expense_amount_text'
        )

        self.main_page_object.assert_element_has_text(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/income_amount_text'),
            expected_text='$0.00',
            error_message='Cannot find income_amount_text'
        )

        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/leftLinesImageView'),
            error_message='Cannot find leftLinesImageView'
        )

        self.main_page_object.assert_element_has_text(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewCategoryName'),
            expected_text='Eating out',
            error_message='Cannot find category name'
        )

        self.main_page_object.assert_element_has_text(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewWholeAmount'),
            expected_text='$5.00',
            error_message='Cannot find textViewWholeAmount'
        )

        self.main_page_object.wait_for_element_and_click(
            by=(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.monefy.app.lite:id/textViewCategoryName" and @text="Eating out"]'),
            error_message='Cannot find text Eating out'
        )

        self.main_page_object.assert_element_has_text(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewTransactionNote'),
            expected_text='coffee',
            error_message='Cannot find textViewTransactionNote'
        )

        self.main_page_object.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewTransactionDate'),
            error_message='Cannot find textViewTransactionDate'
        )


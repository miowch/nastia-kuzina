import unittest


from webdriver import Driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().driver

        self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/imageViewHero'),
            error_message='Cannot find imageViewHero'
        )

        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonContinue'),
            error_message='Cannot find buttonContinue'
        )

        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonClose'),
            error_message='Cannot find buttonClose'
        )

    def test_add_expenses(self):
        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/expense_button'),
            error_message='Cannot find expense_button'
        )
        self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/amount_text'),
            error_message='Cannot find amount_text'
        )
        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/buttonKeyboard5'),
            error_message='Cannot find buttonKeyboard5'
        )
        self.wait_for_element_and_send_keys(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewNote'),
            value='coffee',
            error_message='Cannot find textViewNote'
        )
        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/keyboard_action_button'),
            error_message='Cannot find keyboard_action_button'
        )
        self.wait_for_element_and_click(
            by=(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.monefy.app.lite:id/textCategoryName" and @text="Eating out"]'),
            error_message='Cannot find category Eating out'
        )

        balance_amount_element = self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/balance_amount'),
            error_message='Cannot find balance_amount'
        )
        balance = balance_amount_element.text
        self.assertEqual(balance, 'Balance -$5.00')

        self.wait_for_element_present(
            by=(AppiumBy.XPATH, '//android.widget.TextView[@text="100%"]'),
            error_message='Cannot find text 100%'
        )

        expense_amount_element = self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/expense_amount_text'),
            error_message='Cannot find expense_amount_text'
        )
        expense_amount = expense_amount_element.text
        self.assertEqual(expense_amount, '$5.00')

        income_amount_element = self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/income_amount_text'),
            error_message='Cannot find income_amount_text'
        )
        income_amount = income_amount_element.text
        self.assertEqual(income_amount, '$0.00')

        self.wait_for_element_and_click(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/leftLinesImageView'),
            error_message='Cannot find leftLinesImageView'
        )

        category_name_element = self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewCategoryName'),
            error_message='Cannot find category name'
        )
        category_name = category_name_element.text
        self.assertEqual(category_name, 'Eating out')


        whole_amount_element = self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewWholeAmount'),
            error_message='Cannot find textViewWholeAmount'
        )
        whole_amount = whole_amount_element.text
        self.assertEqual(whole_amount, '$5.00')

        self.wait_for_element_and_click(
            by=(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.monefy.app.lite:id/textViewCategoryName" and @text="Eating out"]'),
            error_message='Cannot find text Eating out'
        )

        transaction_note_element = self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewTransactionNote'),
            error_message='Cannot find textViewTransactionNote'
        )
        transaction_note = transaction_note_element.text
        self.assertEqual(transaction_note, 'coffee')

        self.wait_for_element_present(
            by=(AppiumBy.ID, 'com.monefy.app.lite:id/textViewTransactionDate'),
            error_message='Cannot find textViewTransactionDate'
        )

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def wait_for_element_present(self, by, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)

        return wait.until(
            EC.presence_of_element_located(by),
            message=error_message + '\n')

    def wait_for_element_and_click(self, by, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(by, error_message, timeout_in_sec)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, by, value, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(by, error_message, timeout_in_sec)
        element.send_keys(value)
        return element

    def wait_for_element_not_present(self, by, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)

        return wait.until(
            EC.invisibility_of_element_located(by),
            message=error_message + '\n')

    def wait_for_element_and_clear(self, by, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(by, error_message, timeout_in_sec)
        element.clear()
        return element
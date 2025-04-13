from typing import Final

from appium.webdriver.common.appiumby import AppiumBy

from Task2.utils.ui.main_page_object import MainPageObject


class DashboardPageObject (MainPageObject):
    expenseButton: Final = 'com.monefy.app.lite:id/expense_button'
    sliderButton: Final = 'com.monefy.app.lite:id/leftLinesImageView'
    amountText: Final = 'com.monefy.app.lite:id/amount_text'
    noteInputField: Final = 'com.monefy.app.lite:id/textViewNote'
    chooseCategoryButton: Final = 'com.monefy.app.lite:id/keyboard_action_button'
    balanceAmount: Final = 'com.monefy.app.lite:id/balance_amount'
    expenseAmount: Final = 'com.monefy.app.lite:id/expense_amount_text'
    incomeAmount: Final = 'com.monefy.app.lite:id/income_amount_text'

    keyboardButtonTmpl: str = 'com.monefy.app.lite:id/buttonKeyboard{char}'
    categoryElementTmpl: str = '//android.widget.TextView[@resource-id="com.monefy.app.lite:id/textCategoryName" and @text="{text}"]'
    textElementTmpl: str = '//android.widget.TextView[@text="{text}"]'

    def add_new_expense(self, value, category, note=None):
        self.wait_for_element_and_click(
            by=(AppiumBy.ID, self.expenseButton),
            error_message='Cannot find expense_button'
        )
        self.wait_for_element_present(
            by=(AppiumBy.ID, self.amountText),
            error_message='Cannot find amount_text'
        )

        for char in str(value):
            char = 'Dot' if char == '.' else char
            char = 'Equals' if char == '=' else char
            char = 'Plus' if char == '+' else char
            char = 'Minus' if char == '-' else char
            char = 'Multiply' if char == '*' else char
            char = 'Divide' if char == '/' else char

            self.wait_for_element_and_click(
                by=(AppiumBy.ID, self.keyboardButtonTmpl.replace('{char}', char)),
                error_message=f'Cannot find buttonKeyboard{char}'
            )

        if note is not None:
            self.wait_for_element_and_send_keys(
                by=(AppiumBy.ID, self.noteInputField),
                value=note,
                error_message='Cannot find textViewNote'
            )

        self.wait_for_element_and_click(
            by=(AppiumBy.ID, self.chooseCategoryButton),
            error_message='Cannot find keyboard_action_button'
        )

        self.wait_for_element_and_click(
            by=(AppiumBy.XPATH, self.categoryElementTmpl.replace('{text}', category)),
            error_message=f'Cannot find category {category}'
        )

    def assert_balance(self, expected_balance):
        self.assert_element_has_text(
            by=(AppiumBy.ID, self.balanceAmount),
            expected_text=f'Balance {expected_balance}',
            error_message='Cannot find balance_amount'
        )

    def assert_percentage(self, percentage, occurrence_number=1):
        elements = self.wait_for_elements_present(
            by=(AppiumBy.XPATH, self.textElementTmpl.replace('{text}', percentage)),
            error_message=f'Cannot find text {percentage}'
        )

        return len(elements) == occurrence_number

    def assert_income_and_expense_amounts(self, income_amount, expense_amount):
        error_message='Cannot find text'

        self.assert_element_has_text(
            by=(AppiumBy.ID, self.expenseAmount),
            expected_text=expense_amount,
            error_message=error_message
        )

        self.assert_element_has_text(
            by=(AppiumBy.ID, self.incomeAmount),
            expected_text=income_amount,
            error_message=error_message
        )

    def open_balance_records(self):
        return self.wait_for_element_and_click(
            by=(AppiumBy.ID, self.sliderButton),
            error_message='Cannot find slider button'
        )

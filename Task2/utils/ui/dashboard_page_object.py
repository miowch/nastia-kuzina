from typing import Final

from Task2.utils.ui.main_page_object import MainPageObject


class DashboardPageObject (MainPageObject):
    searchIcon: Final = 'id:com.monefy.app.lite:id/menu_search'
    searchInputField: Final = 'id:com.monefy.app.lite:id/et_search'
    firstSuggestion: Final = 'xpath://android.widget.ListView[@resource-id="com.monefy.app.lite:id/suggestion_list"]/android.widget.RelativeLayout'
    piegraph: Final = 'id:com.monefy.app.lite:id/piegraph'
    expenseButton: Final = 'id:com.monefy.app.lite:id/expense_button'
    incomeButton: Final = 'id:com.monefy.app.lite:id/income_button'
    sliderButton: Final = 'id:com.monefy.app.lite:id/leftLinesImageView'
    amountText: Final = 'id:com.monefy.app.lite:id/amount_text'
    noteInputField: Final = 'id:com.monefy.app.lite:id/textViewNote'
    chooseCategoryButton: Final = 'id:com.monefy.app.lite:id/keyboard_action_button'
    balanceAmount: Final = 'id:com.monefy.app.lite:id/balance_amount'
    expenseAmount: Final = 'id:com.monefy.app.lite:id/expense_amount_text'
    incomeAmount: Final = 'id:com.monefy.app.lite:id/income_amount_text'

    keyboardButtonTmpl: str = 'id:com.monefy.app.lite:id/buttonKeyboard{char}'
    categoryElementTmpl: str = 'xpath://android.widget.TextView[@resource-id="com.monefy.app.lite:id/textCategoryName" and @text="{text}"]'
    textElementTmpl: str = 'xpath://android.widget.TextView[@text="{text}"]'

    def add_expense(self, value, category, note=None):
        self.wait_for_element_and_click(
            self.expenseButton,
            error_message='Cannot find expense_button'
        )
        self.wait_for_element_present(
            self.amountText,
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
                self.keyboardButtonTmpl.replace('{char}', char),
                error_message=f'Cannot find buttonKeyboard{char}'
            )

        if note is not None:
            self.wait_for_element_and_send_keys(
                self.noteInputField,
                value=note,
                error_message='Cannot find textViewNote'
            )

        self.wait_for_element_and_click(
            self.chooseCategoryButton,
            error_message='Cannot find keyboard_action_button'
        )

        self.wait_for_element_and_click(
            self.categoryElementTmpl.replace('{text}', category),
            error_message=f'Cannot find category {category}'
        )

    def add_income(self, value, category, note=None):
        self.wait_for_element_and_click(
            self.incomeButton,
            error_message='Cannot find income_button'
        )
        self.wait_for_element_present(
            self.amountText,
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
                self.keyboardButtonTmpl.replace('{char}', char),
                error_message=f'Cannot find buttonKeyboard{char}'
            )

        if note is not None:
            self.wait_for_element_and_send_keys(
                self.noteInputField,
                value=note,
                error_message='Cannot find textViewNote'
            )

        self.wait_for_element_and_click(
            self.chooseCategoryButton,
            error_message='Cannot find keyboard_action_button'
        )

        self.wait_for_element_and_click(
            self.categoryElementTmpl.replace('{text}', category),
            error_message=f'Cannot find category {category}'
        )

    def assert_balance(self, expected_balance):
        self.assert_element_has_text(
            self.balanceAmount,
            expected_text=f'Balance {expected_balance}',
            error_message='Cannot find balance_amount'
        )

    def assert_percentage(self, percentage, occurrence_number=1):
        elements = self.wait_for_elements_present(
            self.textElementTmpl.replace('{text}', percentage),
            error_message=f'Cannot find text {percentage}'
        )

        return len(elements) == occurrence_number

    def assert_income_and_expense_amounts(self, income_amount, expense_amount):
        error_message='Cannot find text'

        self.assert_element_has_text(
            self.expenseAmount,
            expected_text=expense_amount,
            error_message=error_message
        )

        self.assert_element_has_text(
            self.incomeAmount,
            expected_text=income_amount,
            error_message=error_message
        )

    def open_balance_records(self):
        return self.wait_for_element_and_click(
            self.sliderButton,
            error_message='Cannot find slider button'
        )

    def search(self, query):
        self.wait_for_element_and_click(
            self.searchIcon,
            error_message='Cannot find search icon'
        )
        self.wait_for_element_and_send_keys(
            self.searchInputField,
            value=query,
            error_message='Cannot find search input field'
        )

        self.wait_for_element_and_click(
            self.firstSuggestion,
            error_message='Cannot find suggestion list'
        )

    def assert_piegraph_presence(self):
        self.wait_for_elements_present(
            self.piegraph,
            error_message='Cannot find piegraph'
        )

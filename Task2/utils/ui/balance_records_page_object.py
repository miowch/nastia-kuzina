from typing import Final

import allure

from Task2.utils.ui.main_page_object import MainPageObject


class BalanceRecordsPageObject (MainPageObject):
    categoryName: Final = 'id:com.monefy.app.lite:id/textViewCategoryName'
    wholeCategoryAmount: Final = 'id:com.monefy.app.lite:id/textViewWholeAmount'
    note: Final = 'id:com.monefy.app.lite:id/textViewTransactionNote'
    transactionDate: Final = 'id:com.monefy.app.lite:id/textViewTransactionDate'

    categoryNameEntryTmpl: str = 'xpath://android.widget.TextView[@resource-id="com.monefy.app.lite:id/textViewCategoryName" and @text="{category}"]'

    @allure.step("Check category presents")
    def assert_category_presence(self, category):
        self.assert_element_has_text(
            self.categoryName,
            expected_text=category,
            error_message=f'Cannot find category name {category}'
        )

    @allure.step("Check category amount is correct")
    def assert_category_amount(self, whole_category_amount):
        self.assert_element_has_text(
            self.wholeCategoryAmount,
            expected_text=whole_category_amount,
            error_message=f'Cannot find whole category amount {whole_category_amount}'
        )

    @allure.step("Expand category")
    def expand_category(self, category_name):
        return self.wait_for_element_and_click(
            self.categoryNameEntryTmpl.replace('{category}', category_name),
            error_message=f'Cannot find category {category_name}'
        )

    @allure.step("Check note presents")
    def assert_note_presence(self, note):
        self.assert_element_has_text(
            self.note,
            expected_text=note,
            error_message=f'Cannot find note "{note}"'
        )


    @allure.step("Check there is no note")
    def assert_note_absence(self):
        self.assert_element_has_text(
            self.note,
            expected_text='',
            error_message='Note is present'
        )


    @allure.step("Check transaction date presents")
    def assert_transaction_date_presence(self):
        self.wait_for_element_present(
            self.transactionDate,
            error_message='Cannot find transaction date'
        )

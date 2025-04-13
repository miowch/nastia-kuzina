from typing import Final

from Task2.utils.ui.main_page_object import MainPageObject


class BalanceRecordsPageObject (MainPageObject):
    categoryName: Final = 'id:com.monefy.app.lite:id/textViewCategoryName'
    wholeCategoryAmount: Final = 'id:com.monefy.app.lite:id/textViewWholeAmount'
    note: Final = 'id:com.monefy.app.lite:id/textViewTransactionNote'
    transactionDate: Final = 'id:com.monefy.app.lite:id/textViewTransactionDate'

    categoryNameEntryTmpl: str = 'xpath://android.widget.TextView[@resource-id="com.monefy.app.lite:id/textViewCategoryName" and @text="{category}"]'

    def assert_category_presence(self, category):
        self.assert_element_has_text(
            self.categoryName,
            expected_text=category,
            error_message=f'Cannot find category name {category}'
        )

    def assert_category_amount(self, whole_category_amount):
        self.assert_element_has_text(
            self.wholeCategoryAmount,
            expected_text=whole_category_amount,
            error_message=f'Cannot find whole category amount {whole_category_amount}'
        )

    def expand_category(self, category_name):
        return self.wait_for_element_and_click(
            self.categoryNameEntryTmpl.replace('{category}', category_name),
            error_message=f'Cannot find category {category_name}'
        )

    def assert_note_presence(self, note):
        self.assert_element_has_text(
            self.note,
            expected_text=note,
            error_message=f'Cannot find note "{note}"'
        )

    def assert_transaction_date_presence(self):
        self.wait_for_element_present(
            self.transactionDate,
            error_message='Cannot find transaction date'
        )
from typing import Final

from Task2.utils.ui.main_page_object import MainPageObject


class SearchResultPageObject (MainPageObject):
    subtitle: Final = 'id:com.monefy.app.lite:id/action_bar_subtitle'
    entryTitle: Final = 'id:com.monefy.app.lite:id/title_text_view'
    entryAmount: Final = 'id:com.monefy.app.lite:id/amount_text_view'
    entryDate: Final = 'id:com.monefy.app.lite:id/date_text_view'
    closeButton: Final = 'id:com.monefy.app.lite:id/action_mode_close_button'

    def assert_search_subtitle_is(self, text):
        self.assert_element_has_text(self.subtitle, text, 'Cannot find subtitle')

    def assert_found_category_is(self, text):
        self.assert_element_has_text(self.entryTitle, text, 'Cannot find entry title')

    def assert_entry_amount(self, amount):
        self.assert_element_has_text(self.entryAmount, amount, 'Cannot find entry amount')

    def assert_entry_date_presents(self):
        self.wait_for_element_present(self.entryDate, 'Cannot find entry date')

    def close_search_results(self):
        self.wait_for_element_and_click(self.closeButton, 'Cannot find close button')
from Task2.utils.core_test_case import CoreTestCase
from Task2.utils.ui.dashboard_page_object import DashboardPageObject
from Task2.utils.ui.main_page_object import MainPageObject
from Task2.utils.ui.search_result_page_object import SearchResultPageObject


class TestSearchEntry(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.main_page_object = MainPageObject(self.driver)
        self.dashboard_page_object = DashboardPageObject(self.driver)
        self.search_result_page_object = SearchResultPageObject(self.driver)

    def test_search_by_category(self):
        food_category = 'Food'
        search_query = 'Food'
        self.dashboard_page_object.add_expense('16+4', food_category)
        self.dashboard_page_object.assert_balance('-$20.00')

        self.dashboard_page_object.add_expense(16, 'Clothes')
        self.dashboard_page_object.assert_balance('-$36.00')

        self.dashboard_page_object.search(search_query)

        self.search_result_page_object.assert_search_subtitle_is(search_query)
        self.search_result_page_object.assert_found_category_is(food_category)
        self.search_result_page_object.assert_entry_amount('$20.00')
        self.search_result_page_object.assert_entry_date_presents()

        self.search_result_page_object.close_search_results()

        self.dashboard_page_object.assert_piegraph_presence()
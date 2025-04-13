import allure

from Task2.utils.core_test_case import CoreTestCase
from Task2.utils.ui.balance_records_page_object import BalanceRecordsPageObject
from Task2.utils.ui.dashboard_page_object import DashboardPageObject
from Task2.utils.ui.main_page_object import MainPageObject


class TestAddEntry(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.main_page_object = MainPageObject(self.driver)
        self.dashboard_page_object = DashboardPageObject(self.driver)
        self.balance_records_page_object = BalanceRecordsPageObject(self.driver)

    @allure.title("Add Expenses With Note")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_expenses(self):
        self.dashboard_page_object.add_expense(5, 'Eating out', 'coffee')

        self.dashboard_page_object.assert_balance('-$5.00')
        self.dashboard_page_object.assert_percentage('100%')
        self.dashboard_page_object.assert_income_and_expense_amounts('$0.00', '$5.00')

        self.dashboard_page_object.open_balance_records()

        self.balance_records_page_object.assert_category_presence('Eating out')
        self.balance_records_page_object.assert_category_amount('$5.00')

        self.balance_records_page_object.expand_category('Eating out')

        self.balance_records_page_object.assert_note_presence('coffee')
        self.balance_records_page_object.assert_transaction_date_presence()

    @allure.title("Add Income Without Note")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_income(self):
        self.dashboard_page_object.add_income(2080.59, 'Salary')

        self.dashboard_page_object.assert_balance('$2080.59')
        self.dashboard_page_object.assert_income_and_expense_amounts('$2080.59', '$0.00')

        self.dashboard_page_object.open_balance_records()

        self.balance_records_page_object.assert_category_presence('Salary')

        self.balance_records_page_object.assert_category_amount('$2080.59')

        self.balance_records_page_object.expand_category('Salary')

        self.balance_records_page_object.assert_note_absence()
        self.balance_records_page_object.assert_transaction_date_presence()

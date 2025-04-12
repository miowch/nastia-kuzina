import unittest
from webdriver import Driver


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver().driver

    def test_one(self):
        print("First test run")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

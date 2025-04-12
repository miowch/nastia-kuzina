from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageObject:
    def __init__(self, driver):
        self.driver = driver

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

    def assert_element_has_text(self, by, expected_text, error_message):
        element = self.wait_for_element_present(by, error_message)
        return element.text == expected_text
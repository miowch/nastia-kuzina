from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_locator_by_string(locator_with_type):
    exploded_locator = locator_with_type.split(":", 1)
    locator_strategy = exploded_locator[0]
    locator = exploded_locator[1]

    if locator_strategy == "xpath":
        return AppiumBy.XPATH, locator
    elif locator_strategy == "id":
        return AppiumBy.ID, locator
    else:
        raise ValueError("Cannot get type of locator. Locator: " + locator_strategy)


class MainPageObject:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_present(self, locator, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)
        by = get_locator_by_string(locator)

        return wait.until(
            EC.presence_of_element_located(by),
            message=error_message + '\n')

    def wait_for_elements_present(self, locator, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)
        by = get_locator_by_string(locator)

        return wait.until(
            EC.presence_of_all_elements_located(by),
            message=error_message + '\n')

    def wait_for_element_and_click(self, locator, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(locator, error_message, timeout_in_sec)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, locator, value, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(locator, error_message, timeout_in_sec)
        element.send_keys(value)
        return element

    def wait_for_element_not_present(self, locator, error_message, timeout_in_sec=5):
        wait = WebDriverWait(self.driver, timeout_in_sec)
        by = get_locator_by_string(locator)

        return wait.until(
            EC.invisibility_of_element_located(by),
            message=error_message + '\n')

    def wait_for_element_and_clear(self, locator, error_message, timeout_in_sec=5):
        element = self.wait_for_element_present(locator, error_message, timeout_in_sec)
        element.clear()
        return element

    def assert_element_has_text(self, locator, expected_text, error_message):
        element = self.wait_for_element_present(locator, error_message)
        return element.text == expected_text
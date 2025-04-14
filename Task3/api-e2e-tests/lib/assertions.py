import allure
from requests import Response
import json

class Assertions:
    @staticmethod
    @allure.step("Check JSON contains {key} = {expected_value}")
    def assert_json_value_by_key(response: Response, key, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"

        assert key in response_as_dict, f"Response JSON doesn't have key '{key}"
        assert response_as_dict[key] == expected_value, error_message

    @staticmethod
    @allure.step("Check JSON contains key {key}")
    def assert_json_has_key(response: Response, key):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"

        assert key in response_as_dict, f"Response JSON doesn't have key '{key}"

    @staticmethod
    @allure.step("Check status code is {expected_status_code}")
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    @allure.step("Check JSON doesn't contain key {key}")
    def assert_json_has_not_key(response: Response, key):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"

        assert key not in response_as_dict, f"Response JSON shouldn't have key '{key} but it's present"

    @staticmethod
    @allure.step("Check the server returns error message '{expected_error_message}'")
    def assert_error_message(response: Response, expected_error_message):
        assert response.content.decode() == expected_error_message, \
            f"Unexpected error message: {response.content} instead of {expected_error_message}"
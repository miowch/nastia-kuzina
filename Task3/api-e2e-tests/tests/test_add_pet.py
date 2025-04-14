import random
import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestAddPet (BaseCase):
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Create pet with only required fields, name and photoUrl")
    def test_add_pet_with_only_required_fields(self):
        failed_assertions = []
        data = {
            "name": self.fake.first_name(),
            "photoUrls": ["string"]
        }

        response = MyRequests.post(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 200)
        try:
            Assertions.assert_json_has_key(response, "id")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "name", data["name"], error_message="Pet name differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_has_not_key(
                response, "category")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "photoUrls", data["photoUrls"], error_message="Photo URLs differ from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_has_not_key(
                response, "tags")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_has_not_key(
                response, "status")
        except AssertionError as e:
            failed_assertions.append(str(e))
        if failed_assertions:
            pytest.fail("Soft assertion failures:\n" +
                        "\n".join(failed_assertions))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Create pet with all data")
    def test_add_pet(self):
        failed_assertions = []
        data = self.prepare_pet_creation_data()

        response = MyRequests.post(
            "/pet/",
            data=data)

        Assertions.assert_code_status(response, 200)
        try:
            Assertions.assert_json_value_by_key(
                response, "id", data["id"], error_message="Pet ID differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "name", data["name"], error_message="Pet name differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "category", data["category"], error_message="Pet category differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "photoUrls", data["photoUrls"], error_message="Photo URLs differ from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "tags", data["tags"], error_message="Pet tags differ from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "status", data["status"], error_message="Pet status differs from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        if failed_assertions:
            pytest.fail("Soft assertion failures:\n" +
                        "\n".join(failed_assertions))

    absent_required_fields = [
        ("name"),
        ("photoUrls")
    ]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to create pet without required field")
    @pytest.mark.parametrize("absent_required_field", absent_required_fields)
    def test_add_pet_without_required_field(self, absent_required_field):
        data = self.prepare_pet_creation_data()
        data.pop(absent_required_field)

        response = MyRequests.post(
            "/pet/",
            data=data)

        Assertions.assert_code_status(response, 400)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Try to create pet without already existing ID")
    def test_add_pet_with_existing_id(self):
        response1 = self.create_pet()
        existing_id = self.get_json_value(response1, "id")

        new_pet_data2 = {
            "id": existing_id,
            "name": self.fake.first_name(),
            "photoUrls": ["string"]
        }

        response2 = MyRequests.post(
            "/pet/",
            data=new_pet_data2)

        Assertions.assert_code_status(response2, 400)

    invalid_ids = [
        ("15"),
        ("two"),
        ("2.5")
    ]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to create pet with invalid ID")
    @pytest.mark.parametrize("invalid_id", invalid_ids)
    def test_add_pet_with_invalid_id(self, invalid_id):
        data = {
            "id": invalid_id,
            "name": self.fake.first_name(),
            "photoUrls": ["string"]
        }

        response = MyRequests.post(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    invalid_names = [
        (400),
        (True)
    ]

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Try to create pet with invalid name")
    @pytest.mark.parametrize("invalid_name", invalid_names)
    def test_add_pet_with_invalid_name(self, invalid_name):
        data = {
            "id": random.randint(1, 1000),
            "name": invalid_name,
            "photoUrls": ["string"]
        }

        response = MyRequests.post(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to create pet with invalid status")
    def test_add_pet_with_invalid_status(self):
        data = {
            "id": random.randint(1, 1000),
            "name": self.fake.first_name(),
            "photoUrls": ["string"],
            "status": "wrong"
        }

        response = MyRequests.post(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Try to create pet with invalid photoUrl")
    def test_add_pet_with_invalid_photoUrls(self):
        data = {
            "id": random.randint(1, 1000),
            "name": self.fake.first_name(),
            "photoUrls": ("string", 2, 7)
        }

        response = MyRequests.post(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to create pet with invalid parameter")
    def test_add_pet_with_invalid_parameter(self):
        data = {
            "id": random.randint(1, 1000),
            "name": self.fake.first_name(),
            "owner": self.fake.name()
        }

        response = MyRequests.post(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

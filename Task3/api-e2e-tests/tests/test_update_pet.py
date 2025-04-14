import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUpdatePet (BaseCase):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Update pet with only required data")
    def test_update_pet(self):
        failed_assertions = []
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")

        new_data = {
            "id": pet_id,
            "name": self.fake.first_name(),
            "photoUrls": ["gewd_boy.png"]
        }

        response = MyRequests.put(
            "/pet/",
            new_data)

        Assertions.assert_code_status(response, 200)
        try:
            Assertions.assert_json_value_by_key(
                response, "id", pet_id, error_message="Pet ID differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "name", new_data["name"], error_message="Pet name differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(
                response, "photoUrls", new_data["photoUrls"], error_message="Photo URLs differ from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_has_not_key(response, "category")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_has_not_key(response, "tags")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_has_not_key(response, "status")
        except AssertionError as e:
            failed_assertions.append(str(e))
        if failed_assertions:
            pytest.fail("Soft assertion failures:\n" +
                        "\n".join(failed_assertions))

        updated_pet = self.get_pet(pet_id)
        assert updated_pet.json() == new_data

    absent_required_fields = [
        ("id"),
        ("name"),
        ("photoUrls")
    ]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to update pet without required field {absent_required_field}")
    @pytest.mark.parametrize("absent_required_field", absent_required_fields)
    def test_update_pet_without_required_field(self, absent_required_field):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")

        new_data = {
            "id": pet_id,
            "name": self.fake.first_name(),
            "photoUrls": ["gewd_boy.png"]
        }
        new_data.pop(absent_required_field)

        response = MyRequests.put(
            "/pet/",
            new_data)

        Assertions.assert_code_status(response, 400)

    invalid_ids = [
        (False),
        ("two"),
        ("2.5")
    ]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to update pet with invalid ID {invalid_id}")
    @pytest.mark.parametrize("invalid_id", invalid_ids)
    def test_update_pet_with_invalid_id(self, invalid_id):
        data = {
            "id": invalid_id,
            "name": self.fake.first_name(),
            "photoUrls": ["string"]
        }

        response = MyRequests.put(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 400)

    invalid_names = [
        (400),
        (True)
    ]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to update pet with invalid name {invalid_name}")
    @pytest.mark.parametrize("invalid_name", invalid_names)
    def test_update_pet_with_invalid_name(self, invalid_name):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        data = {
            "id": pet_id,
            "name": invalid_name,
            "photoUrls": ["string"]
        }

        response = MyRequests.put(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to update pet with invalid status")
    def test_update_pet_with_invalid_status(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        data = {
            "id": pet_id,
            "name": self.fake.first_name(),
            "photoUrls": ["string"],
            "status": "wrong"
        }

        response = MyRequests.put(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to update pet with invalid photoUrl")
    def test_update_pet_with_invalid_photoUrls(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        data = {
            "id": pet_id,
            "name": self.fake.first_name(),
            "photoUrls": ("string", 2, 7)
        }

        response = MyRequests.put(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to update pet with invalid parameter")
    def test_update_pet_with_invalid_parameter(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        data = {
            "id": pet_id,
            "name": self.fake.first_name(),
            "owner": self.fake.name()
        }

        response = MyRequests.put(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 405)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Try to update pet with non-existing ID")
    def test_update_pet_with_nonexisting_id(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        self.delete_pet(pet_id)

        data = {
            "id": pet_id,
            "name": self.fake.first_name(),
            "photoUrls": ["string"]
        }

        response = MyRequests.put(
            "/pet/",
            data)

        Assertions.assert_code_status(response, 404)
        Assertions.assert_error_message(response, "Pet not found")

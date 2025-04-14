import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestDeletePet (BaseCase):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Try to delete pet by ID")
    def test_delete_pet(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")

        response = MyRequests.delete(
            f"/pet/{pet_id}")

        Assertions.assert_code_status(response, 200)

        response2 = self.get_pet(pet_id)
        Assertions.assert_code_status(response2, 404)

    invalid_ids = [
        (False),
        ("two"),
        ("2.5")
    ]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Try to delete pet by invalid ID")
    @pytest.mark.parametrize("invalid_id", invalid_ids)
    def test_delete_pet_with_invalid_id(self, invalid_id):
        response = MyRequests.delete(
            f"/pet/{invalid_id}"
        )

        Assertions.assert_code_status(response, 400)
        Assertions.assert_error_message(response, 'Invalid pet value')

    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Try to delete pet by non-existing ID")
    def test_delete_nonexisting_pet(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        self.delete_pet(pet_id)

        response = MyRequests.delete(f"/pet/{pet_id}")
        Assertions.assert_code_status(response, 200)

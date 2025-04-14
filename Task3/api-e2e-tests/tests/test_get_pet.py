from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestGetPet (BaseCase):
    def test_get_pet_by_id(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")

        response = MyRequests.get(f"/pet/{pet_id}")

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_key(response, "name", pet.json()["name"], "Pet name differs from expected one")

    def test_get_pet_by_invalid_id(self):
        response = MyRequests.get(f"/pet/one")

        Assertions.assert_code_status(response, 400)
        Assertions.assert_error_message(response, "Invalid ID supplied")

    def test_get_pet_by_nonexisting_id(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        self.delete_pet(pet_id)

        response = MyRequests.get(f"/pet/{pet_id}")
        Assertions.assert_code_status(response, 404)
        Assertions.assert_error_message(response, "Pet not found")

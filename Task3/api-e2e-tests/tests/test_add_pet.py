import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

class TestAddPet(BaseCase):
    absent_required_fields = [
         ("name"),
         ("photoUrls")
    ]

    def test_add_pet(self):
        failed_assertions = []
        data = self.prepare_pet_creation_data()

        response = MyRequests.post(
            "/pet/",
            data=data)
        
        Assertions.assert_code_status(response, 200)
        try:
            Assertions.assert_json_value_by_key(response, "id", data["id"], error_message="Pet ID differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(response, "name", data["name"], error_message="Pet name differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))    
        try:
            Assertions.assert_json_value_by_key(response,"category", data["category"], error_message="Pet category differs from expected one")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(response, "photoUrls", data["photoUrls"], error_message="Photo URLs differ from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(response, "tags", data["tags"], error_message="Pet tags differ from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        try:
            Assertions.assert_json_value_by_key(response, "status", data["status"], error_message="Pet status differs from expected ones")
        except AssertionError as e:
            failed_assertions.append(str(e))
        if failed_assertions:
            pytest.fail("Soft assertion failures:\n" + "\n".join(failed_assertions))

    @pytest.mark.parametrize("absent_required_field", absent_required_fields)
    def test_add_pet_without_required_field(self, absent_required_field):
        data = self.prepare_pet_creation_data()
        data.pop(absent_required_field)

        response = MyRequests.post(
            "/pet/",
            data=data)
        
        Assertions.assert_code_status(response, 400)

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







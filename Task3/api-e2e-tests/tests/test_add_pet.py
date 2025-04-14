from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

class TestAddPet(BaseCase):
    def test_add_pet(self):
        new_pet_data = {
            "name": "doggie",
            "category": {
                "id": 1,
                "name": "Dogs"
            },
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
        }
        response = MyRequests.post(
            "/pet/",
            data=new_pet_data)
        
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_json_value_by_name(response, "name", "doggie")
        Assertions.assert_json_value_by_name(response, "photoUrls", ["string"])

    def test_add_pet_with_existing_id(self):
        new_pet_data1 = {
            "name": "Oscar",
            "photoUrls": ["string"]
        }
        response1 = MyRequests.post(
            "/pet/",
            data=new_pet_data1)
        
        Assertions.assert_code_status(response1, 200)
        existing_id = self.get_json_value(response1, "id")

        new_pet_data2 = {
            "id": existing_id,
            "name": "Oscar",
            "photoUrls": ["string"]
        }

        response2 = MyRequests.post(
            "/pet/",
            data=new_pet_data2)
        
        Assertions.assert_code_status(response2, 400)







import json.decoder
import random

import allure
from faker import Faker
from requests import Response

from lib.my_requests import MyRequests


class BaseCase:
    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]
    
    fake = Faker()

    @allure.step("Prepare pet creation data")
    def prepare_pet_creation_data(self):
        return {
            "id": random.randint(1, 100),
            "name": self.fake.first_name(),
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
                "name": "tag1"
                }
            ],
            "status": "available"
        }
    
    @allure.step("Create pet")
    def create_pet(self):
        data = self.prepare_pet_creation_data()

        return MyRequests.post(
            "/pet/",
            data=data)
    
    @allure.step("Get pet")
    def get_pet(self, id):
        return MyRequests.get(
            f"/pet/{id}")

    @allure.step("Delete pet")
    def delete_pet(self, pet_id):
        return MyRequests.delete(f"/pet/{pet_id}")
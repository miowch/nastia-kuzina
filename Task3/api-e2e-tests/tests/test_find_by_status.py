import random
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestFindByStatus (BaseCase):
    def test_find_pets_by_status(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        pet_status = self.get_json_value(pet, "status")

        response = MyRequests.get(f"/pet/findByStatus?status={pet_status}")

        Assertions.assert_code_status(response, 200)

        found_pet_ids = []
        for p in response.json():
            found_pet_ids.append(p["id"])
            assert p["status"] == pet_status, "Found pet has status that differs from the one in query!"
        
        assert pet_id in found_pet_ids
            

    def test_find_pets_by_multiple_statuses(self):
        pet1 = self.create_pet()
        pet_id1 = self.get_json_value(pet1, "id")
        pet_status1 = self.get_json_value(pet1, "status")

        pet_data2 = {
            "id": random.randint(1, 1000),
            "name": self.fake.first_name(),
            "photoUrls": ["string"],
            "status": "pending"
        }
        pet2 = MyRequests.post("/pet/", pet_data2)
        pet_id2 = self.get_json_value(pet2, "id")
        pet_status2 = self.get_json_value(pet2, "status")

        response = MyRequests.get(f"/pet/findByStatus?status={pet_status1},{pet_status2}")

        Assertions.assert_code_status(response, 200)

        found_pet_ids = []
        for p in response.json():
            found_pet_ids.append(p["id"])
            assert p["status"] == pet_status1 or p["status"] == pet_status2, "Found pet has status that differs from the ones in query!"
        
        assert pet_id1 in found_pet_ids
        assert pet_id2 in found_pet_ids

    def test_find_pets_by_empty_status(self):
        response = MyRequests.get(f"/pet/findByStatus")

        Assertions.assert_code_status(response, 400)
        Assertions.assert_error_message(response, "No status provided. Try again?")
        

    def test_find_pets_by_incorrect_status(self):
        incorrect_status = "free"
        response = MyRequests.get(f"/pet/findByStatus?status={incorrect_status}")

        Assertions.assert_code_status(response, 400)
        Assertions.assert_error_message(response, f"Input error: query parameter `status value `{incorrect_status}` is not in the allowable values `[available, pending, sold]`")

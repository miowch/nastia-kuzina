import random
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestFindByTag (BaseCase):
    def test_find_pets_by_tag(self):
        pet = self.create_pet()
        pet_id = self.get_json_value(pet, "id")
        pet_tag = self.get_json_value(pet, "tags")

        response = MyRequests.get(f"/pet/findByTags?tags={pet_tag[0]}")

        Assertions.assert_code_status(response, 200)

        found_pet_ids = []
        for p in response.json():
            found_pet_ids.append(p["id"])
            assert pet_tag[0] in p["tags"], "Found pet has tags that differ from the one in query!"
        
        assert pet_id in found_pet_ids
            

    def test_find_pets_by_multiple_tags(self):
        pet1 = self.create_pet()
        pet_id1 = self.get_json_value(pet1, "id")
        pet_tag1 = self.get_json_value(pet1, "tags")

        pet_data2 = {
            "id": random.randint(1, 1000),
            "name": self.fake.first_name(),
            "photoUrls": ["string"],
            "tags": [{"id": 1, "name": "tag1"}]
        }
        pet2 = MyRequests.post("/pet/", pet_data2)
        pet_id2 = self.get_json_value(pet2, "id")
        pet_tag2 = self.get_json_value(pet2, "tags")

        response = MyRequests.get(f"/pet/findByTags?tags={pet_tag1[0]},{pet_tag2[0]}")

        Assertions.assert_code_status(response, 200)

        found_pet_ids = []
        for p in response.json():
            found_pet_ids.append(p["id"])
            assert pet_tag1[0] in p["tags"] or pet_tag2[0] in p["tags"], "Found pet has tags that differ from the one in query!"
        
        assert pet_id1 in found_pet_ids
        assert pet_id2 in found_pet_ids

    def test_find_pets_by_empty_tag(self):
        response = MyRequests.get(f"/pet/findByTags")

        Assertions.assert_code_status(response, 400)
        Assertions.assert_error_message(response, "No tags provided. Try again?")

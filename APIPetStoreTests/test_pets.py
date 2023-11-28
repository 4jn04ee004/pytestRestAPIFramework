import pytest

from utils.myConfigParser import *
from utils.myUtils import get_api_data, put_api_data
import random
import string


# baseURL = "https://petstore.swagger.io/v2/pet/"
petID = "191"
updated_pet_id = "200"
baseURL = return_pet_api_url()


def test_get_pet_by_id_response():
    url = baseURL + petID
    data, status_code, time_elapsed = get_api_data(url)
    assert data["id"] == int(petID)
    assert status_code == 200
    print("Time Taken : ", time_elapsed)


@pytest.mark.repeat(1000)
def test_update_pet_by_id():
    url = baseURL
    payload = {
        "id": int(updated_pet_id),
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": random.choice(string.ascii_letters),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "pending"
    }
    data, status_code, time_elapsed = put_api_data(url, payload)
    print(status_code)
    assert data["id"] == int(updated_pet_id)
    assert status_code == 200
    print("Time Taken : ", time_elapsed)

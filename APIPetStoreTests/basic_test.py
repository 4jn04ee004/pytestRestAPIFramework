import pytest
import requests, json
import random

baseURI = "https://petstore.swagger.io/v2/pet/"
petID = random.randint(100, 160)


def test_getPetByID_Response():
    """
    This is a test function which provides the response
    based on the pet ID.
    :return: 200 Ok
    """
    url = baseURI + str(petID)
    headers = {
        "Content-Type": "application/json"
    }
    print("\nRequest URL :", url)
    res = requests.get(url, verify=False, headers=headers)
    data = res.json()
    print(json.dumps(data, indent=4))
    assert len(data) > 0, "Response is Empty"

def test_add_new_pet_in_the_store():
    """
    This is a test function which provides the response
    based on the pet ID.
    :return: 200 Ok
    """
    url = baseURI
    header = {'Content-Type': 'application/json'}
    payload = {"id": petID,"name": "doggie","status": "available"}
    print("\nRequest URL :", url)
    res = requests.post(url, json=payload, verify=False, headers=header)
    data = res.json()
    print(res.status_code)
    print(json.dumps(data, indent=4))
    pytest.globalvar = data["id"]
    assert data["id"] == petID, f"Pet with ID {petID} not added"
    return data["id"]


def test_getPetById():
    """
        This is a test function which provides the response
        based on the pet ID.
        :return: 200 Ok
        """
    petID = pytest.globalvar

    url = baseURI + str(petID)
    headers = {
        "Content-Type": "application/json"
    }
    print("\nRequest URL :", url)
    res = requests.get(url, verify=False, headers=headers)
    data = res.json()
    print(json.dumps(data, indent=4))

    assert data["id"] == petID, f"Pet with ID {petID} not found"



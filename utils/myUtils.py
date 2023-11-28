import requests, json


def get_api_data(url):
    headers = {
        "Content-Type": "application/json"
    }
    print("Requested URL : ", url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, "Empty Response"
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken


def put_api_data(url, payload):
    headers = {
        "Content-Type": "application/json"
    }
    print("Requested URL : ", url)

    response = requests.put(url, verify=False, headers=headers, json=payload)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken

import requests
import json


class FetchDataFromCIForCVIM():
    def __init__(self, obj):
        self.obj = obj
        self.baseurl = "https://stg-rcppb.int.rmn-rmpkiba.local/central-inventory/rest/entity"
        self.headers = headers = {
            'content-type': 'application/json',
        }

    def get_ran_location(self, obj):
        params = {
            'name.eq': f'{self.obj}',
        }
        resp = requests.get(self.baseurl, params=params, headers=self.headers, verify=False)
        if resp.status_code not in (400, 404, 500, 503):
            return resp.text, resp.status_code
        else:
            raise ConnectionError("CI Not Reachable")






import json

data = {
    "name": "Alok Kumar",
    "age": None,
    "Employment": {"Company Name": "Rakuten Inc",
                   "Employment Type": "Seconded",
                   "Salary": None,
                   "Permanent": True}
}

my_json_data = json.dumps(data, sort_keys=False, indent=4)
print(my_json_data)
import requests, json

API_URL = 'http://localhost:8001/api/Category/get-all'


# data = {'s': 's'}
# json_data = json.dump(data)
# print(json_data)
# response = requests.post(api_url, data=json_data, headers={'Content-Type': 'application/json'})

def get_response(url):
    return requests.get(url)


def deserializer(data):
    return json.loads(data)

import requests
import json
status='available'
headers={
    'accept': 'application/json',
    'Content-Type' : 'application/json'
}
params={'status': 'available'}
base_url = 'https://petstore.swagger.io/v2'
# GET запрос
res = requests.get(f"{base_url}/pet/findByStatus", params=params, headers=headers)
print(res.status_code)
# print(res.json())
data ={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
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
data=json.dumps(data)
# PUT запрос
res = requests.put(f"{base_url}/pet", headers=headers, data = data)
print(res.status_code)
print(res.json())
petID= res.json()
petID = list(petID.values())[0]
# print(petID)
headers={
    'accept': 'application/json'}
# POST запрос
res = requests.post(f"{base_url}/pet/{petID}",  headers=headers, data = data)
print(res.status_code)
print(res.json())
# DELETE запрос
res = requests.delete(f"{base_url}/pet/{petID}")
print(res.status_code)
print(res.json())

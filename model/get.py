import requests
api_url = "http://localhost:5000/user"
response = requests.get(api_url)
response.json()
print(response.json())
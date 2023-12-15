import requests
api_url = "http://localhost:5000/user"
newUser = {'username': 'userB', 'password': 'bbb'}
response = requests.post(api_url, json=newUser)
print(response.status_code)
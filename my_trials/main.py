# ----------------------GET----------------------

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# api_irl = "http://natu-social.herokuapp.com/"
# response = requests.get(api_irl)
# print(response.status_code)
# print(response.json())

#------------------POST------------------------
import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())
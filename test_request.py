import requests
response = requests.get("http://0.0.0.0:5000")
print(f"Json response is : {response.json()}")
json_key_message = (response.json())["message"]
print(f"Accessing json key : {json_key_message}")

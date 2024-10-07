import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)
responses = response.json()

print(responses)
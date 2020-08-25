import requests

url = "http://0.0.0.0:8080/healthz"

payload = "{\n    \"name\":\"Denem\"\n\n\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

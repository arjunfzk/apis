import requests

url = "https://api.ambiverse.com/v1/entitylinking/analyze"

payload = "{\"text\" : \"Ma founded Alibaba in Hangzhou with investments from SoftBank and Goldman.\"}"
headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'authorization': "20e66461: 20aca28bd8ca9e809e3c41ca76edc9ee "
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
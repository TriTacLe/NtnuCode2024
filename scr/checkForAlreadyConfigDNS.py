#koden vil liste alle DNS-oppføringer for domenet ditt for å se hva som allerede er konfigurert

import requests
from requests.auth import HTTPBasicAuth

API_TOKEN = "heytDI6dBJVcUQHV"
API_SECRET = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs"
DOMAIN_ID = 2089158

url = f"https://api.domeneshop.no/v0/domains/{DOMAIN_ID}/dns"
response = requests.get(url, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))

if response.status_code == 200:
    print("Current DNS Records:")
    for record in response.json():
        print(record)
else:
    print("Failed to fetch DNS records:", response.status_code, response.json())

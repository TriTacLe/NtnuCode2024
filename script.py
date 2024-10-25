import requests
from requests.auth import HTTPBasicAuth

# Dine Domeneshop autentiseringsdetaljer
token = "heytDI6dBJVcUQHV"
secret = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs"

# Domeneshop API-endepunkt
url = "https://api.domeneshop.no/v0/domains"

# Send forespørsel med autentisering
response = requests.get(url, auth=HTTPBasicAuth(token, secret))

# Sjekk responsstatus og innhold
if response.status_code == 200:
    print("Autentisering vellykket!")
    print("Data:", response.json())
else:
    print(f"Autentisering feilet med statuskode: {response.status_code}")
    print("Feilmelding:", response.text)

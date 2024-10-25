import requests
from requests.auth import HTTPBasicAuth

# API autentiseringsdetaljer
API_TOKEN = "heytDI6dBJVcUQHV"
API_SECRET = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs"

# Endepunkt for å liste opp domener
url = "https://api.domeneshop.no/v0/domains"

# Send forespørsel med autentisering
response = requests.get(url, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))

# Sjekk responsstatus og innhold
if response.status_code == 200:
    print("Domeneliste hentet:")
    print(response.json())
else:
    print("Kunne ikke hente domeneliste.")
    print("Statuskode:", response.status_code)
    print("Respons:", response.json())

import requests
from requests.auth import HTTPBasicAuth

#API autentiseringsdetaljer, ressurser som trengs
API_TOKEN = "heytDI6dBJVcUQHV"
API_SECRET = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs"

#endepunkt for å liste opp domener
url = "https://api.domeneshop.no/v0/domains"
#url = "https://{API_TOKEN}:{API_SECRET}@api.domeneshop.no/v0/dyndns/update?hostname=codexenmo.no&myip=127.0.0.1"


#send forespørsel med autentisering
response = requests.get(url, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))

#check responsstatus og innhold
if response.status_code == 200: #200 er statuskode for http
    print("Domeneliste hentet:")
    print(response.json())
else:
    print("Kunne ikke hente domeneliste.")
    print("Statuskode:", response.status_code)
    print("Respons:", response.json())

    
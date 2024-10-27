import requests
from requests.auth import HTTPBasicAuth

#domeneshop api-autentisering
API_TOKEN = "heytDI6dBJVcUQHV"
API_SECRET = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs"
DOMAIN_ID = 2089158  #IP for codexenmo.no

#sjekke om en DNS-oppføring allerede eksisterer
"""
def get_existing_record(subdomain):
    #url = f"https://api.domeneshop.no/v0/domains/{DOMAIN_ID}/dns"
    url = f"https://{API_TOKEN}:{API_SECRET}@api.domeneshop.no/v0/dyndns/update?hostname=codexenmo.no&myip=127.0.0.1"
    response = requests.get(url, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))
    if response.status_code == 200:
        try:
            records = response.json()
            for record in records:
                if record["host"] == subdomain and record["type"] == "A":
                    return record
        except requests.exceptions.JSONDecodeError:
            print("Failed to parse JSON response")
    return None

#oppdatere/opprette DNS-oppføringen til en spesifikk Raspberry Pi
def update_dns_record(subdomain, ip_address):
    existing_record = get_existing_record(subdomain)
    headers = {"Content-Type": "application/json"}
    data = {
        "host": subdomain,  #subdomene, ex: rpi1, rpi2, nedenfor brukes tri
        "type": "A",        #type A-oppføring for IPv4 søk opp
        "data": ip_address,
        "ttl": 3600         #time to live satt til 1 time
    }
"""
#DDNS oppdatering ikke oppretting
def update_ddns(subdomain, ip_address=None):
    #DDNS-URL for dynamisk IP-oppdatering
    url = f"https://{API_TOKEN}:{API_SECRET}@api.domeneshop.no/v0/dyndns/update?hostname={subdomain}.codexenmo.no"
    
    if ip_address:
        url += f"&myip={ip_address}"
    
    #GET-forespørsel til DDNS-endepunktet
    response = requests.get(url)
    
    #sjekk responsstatus og logg resultatet
    if response.status_code in [200, 204]:  # Nå regner vi også 204 som en suksess
        print(f"IP for {subdomain}.codexenmo.no updated/created to {ip_address if ip_address else 'public IP'} via DDNS")

    else:
        print("Failed to update DNS record:", response.status_code, response.text)

    #put og post
    """
    if existing_record:
        #hvis oppføringen finnes, oppdater den med PUT
        url = f"https://api.domeneshop.no/v0/domains/{DOMAIN_ID}/dns/{existing_record['id']}"
        response = requests.put(url, json=data, headers=headers, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))
    else:
        #hvis oppføringen ikke finnes, opprett den med POST
        #url = f"https://api.domeneshop.no/v0/domains/{DOMAIN_ID}/dns"
        url = f"https://{API_TOKEN}:{API_SECRET}@api.domeneshop.no/v0/dyndns/update?hostname=codexenmo.no&myip=127.0.0.1"
        response = requests.post(url, json=data, headers=headers, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))

    #kontroller respons og logg resultatet
    if response.status_code in [200, 201]:
        print(f"DNS record for {subdomain}.codexenmo.no updated/created to {ip_address}")
    elif response.status_code == 204:
        print(f"DNS-record for {subdomain}.codexenmo.no updated (no content returned).")
    else:
        #bruk .text for å vise responsen hvis JSON-dekoding feiler
        try:
            print("Failed to update DNS record:", response.status_code, response.json())
        except requests.exceptions.JSONDecodeError:
            print("Failed to update DNS record:", response.status_code, response.text)
    """

#eksempel på oppdatering av subdomener med unike IP-er
devices = {
    "TriTest1": "192.168.1.101",
    "TriTest2": "192.168.1.102", 
    "Tri": "51.120.13.200",
    #"broadcast": "192.168.1.255",
    "broadcast": "192.168.1.133",

}

#oppdater hver Raspberry Pi sitt subdomene med den aktuelle IP-adressen
for subdomain, ip in devices.items():
    #update_dns_record(subdomain, ip)
    update_ddns(subdomain, ip)

#gammel kommentar til eldre kode, ikke fjern da det er logg
###VIKTIG!!!: hvis "no content" return betyr det at subdomain navnet allerde eksiterer
###Hvis "no content" ikke kommer opp, men en "to IP" betyr at DNS-oppføringen for subdomen navnet ble enten opprettet/oppdatert med IP og API-et returnerte en bekreftelse 
#(200 eller 201 status) som inneholdt innhold i JSON-format.
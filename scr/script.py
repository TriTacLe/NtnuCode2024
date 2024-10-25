"""
For å sette opp dynamisk DNS med Domeneshop sitt API for å automatisk oppdatere DNS-registreringer når IP-adressen endrer seg, 
kan du implementere et Python-skript som kjører på din VM i Azure. 
Dette skriptet vil overvåke IP-adressene til de tilkoblede Raspberry Pi-enhetene og oppdatere DNS-oppføringene på Domeneshop for å peke til de riktige IP-adressene.
"""
"""
Dette programmet vil bruke Domeneshop API til å oppdatere A-oppføringer for hver Raspberry Pi med unike subdomener som rpi1.codexenmo.no, rpi2.codexenmo.no, osv.
"""

import requests
from requests.auth import HTTPBasicAuth
import json

#Domeneshop API-autentisering
API_TOKEN = "heytDI6dBJVcUQHV" #trenger
API_SECRET = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs" #trenger
DOMAIN_ID =  2089158 #ID for codexemno.no trenger hent fra Domeneshop, generet av finneDomener 

#domeneshop API
url = "https://api.domeneshop.no/v0/domains"
url_2 = "https://{token}:{secret}@api.domeneshop.no/v0/dyndns/update?hostname=.codexenmo.no&myip=127.0.0.1"

#funksjon for å oppdatere DNS-oppføringen til en spesifikk Raspberry Pi
def update_dns_record(subdomain, ip_address):
    url = f"https://api.domeneshop.no/v0/domains/{DOMAIN_ID}/dns"
    headers = {"Content-Type": "application/json"}
    data = {
        "host": subdomain,  #subdomene ex rpi1, rpi2
        "type": "A",        #type A-oppføring for IPv4
        "data": ip_address,
        "ttl": 3600         #TTL satt til 1 time
    }

    #API-forespørsel for oppdatering/opprette DNS overføringen
    response = requests.post(url, json=data, headers=headers, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))
    if response.status_code == 200:
        print(f"DNS record for {subdomain}.codexenmo.no updated to {ip_address}")
    else:
        print("Failed to update DNS record:", response.status_code, response.json())

#ex
#oppdater subdomener med aktuelle IP-er, kan slettes til slutt. 
devices = {
    "rpi1": "192.168.1.101", #eksempel bare
    "rpi2": "192.168.1.102", #eksempel bare
}

#oppdater hver RPi sitt subdomene med den aktuelle IP-adressen
for subdomain, ip in devices.items():
    update_dns_record(subdomain, ip)

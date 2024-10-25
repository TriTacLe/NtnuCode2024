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

# Domeneshop API-autentisering
API_TOKEN = #trenger
API_SECRET = #trenger
DOMAIN_ID =  #trenger hent fra Domeneshop 

#funksjon for å oppdatere DNS-oppføringen til en spesifikk Raspberry Pi
def update_dns_record(subdomain, ip_address):
    url = f"https://api.domeneshop.no/v0/domains/{DOMAIN_ID}/dns"
    headers = {"Content-Type": "application/json"}
    data = {
        "host": subdomain,  # subdomene f.eks. rpi1, rpi2
        "type": "A",        # type A-oppføring for IPv4
        "data": ip_address,
        "ttl": 3600         # TTL satt til 1 time
    }

    #API-forespørsel
    response = requests.post(url, json=data, headers=headers, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))
    if response.status_code == 200:
        print(f"DNS record for {subdomain}.codexenmo.no updated to {ip_address}")
    else:
        print("Failed to update DNS record:", response.status_code, response.json())

#ex
#oppdater subdomener med aktuelle IP-er
devices = {
    "rpi1": "192.168.1.101", #eksempel bare
    "rpi2": "192.168.1.102", #eksempel bare
}

for subdomain, ip in devices.items():
    update_dns_record(subdomain, ip)

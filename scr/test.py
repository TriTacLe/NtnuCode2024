import subprocess
import requests
from requests.auth import HTTPBasicAuth

# Domeneshop API authentication
API_TOKEN = "heytDI6dBJVcUQHV"
API_SECRET = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs"
DOMAIN_ID = 2089158  # ID for codexenmo.no

# SSH commands to retrieve IP address, hostname, and model info
def get_ip_and_domain_from_pi():
    ip_command = "hostname -I | awk '{print $1}'"
    domain_command = "hostname --fqdn"
    model_command = "cat /proc/cpuinfo | grep 'Model'"

    try:
        ip_address = subprocess.check_output(ip_command, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        ip_address = "Unable to retrieve IP"

    try:
        domain_name = subprocess.check_output(domain_command, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        domain_name = "Unable to retrieve domain name"

    try:
        model_info = subprocess.check_output(model_command, shell=True).decode().strip()
        is_raspberry_pi = 'Raspberry Pi' in model_info
    except subprocess.CalledProcessError:
        model_info = "Unable to retrieve model information"
        is_raspberry_pi = False

    return domain_name, ip_address, is_raspberry_pi

# DDNS update function
def update_ddns(subdomain, ip_address):
    url = f"https://{API_TOKEN}:{API_SECRET}@api.domeneshop.no/v0/dyndns/update?hostname={subdomain}.codexenmo.no&myip={ip_address}"
    
    response = requests.get(url)
    
    if response.status_code in [200, 204]:
        print(f"IP for {subdomain}.codexenmo.no updated to {ip_address} via DDNS")
    else:
        print("Failed to update DNS record:", response.status_code, response.text)

# Fetch and update DNS for Raspberry Pi device
domain, ip, is_raspberry_pi = get_ip_and_domain_from_pi()

if is_raspberry_pi and ip != "Unable to retrieve IP" and domain != "Unable to retrieve domain name":
    update_ddns(domain.split('.')[0], ip)  # Pass only the subdomain part to update_ddns
else:
    print("Unable to update DNS. Check device info or IP retrieval.")

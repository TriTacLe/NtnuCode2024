import requests
from requests.auth import HTTPBasicAuth

API_TOKEN = "heytDI6dBJVcUQHV"
API_SECRET = "ekNjmFzmJZ3Y9noTVvwavcKRo6NH3G5s09vDfeJhj9KpCOlKQsELruoTNuohFKNs"
DOMAIN_ID = 2089158  #ID for codexenmo.no

#slett oppføringer for subdomener som argument
def delete_existing_records(hostnames):
    url = f"https://api.domeneshop.no/v0/domains/{DOMAIN_ID}/dns"
    response = requests.get(url, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))
    
    if response.status_code == 200:
        records = response.json()
        for record in records:
            if record["host"] in hostnames:
                delete_url = f"{url}/{record['id']}"
                delete_response = requests.delete(delete_url, auth=HTTPBasicAuth(API_TOKEN, API_SECRET))
                if delete_response.status_code == 204:
                    print(f"Deleted record for {record['host']}")
                else:
                    print(f"Failed to delete record {record['host']}: {delete_response.status_code}")
    else:
        print("Failed to fetch DNS records:", response.status_code, response.json())

delete_existing_records(["Tri2", "TriTest2"])

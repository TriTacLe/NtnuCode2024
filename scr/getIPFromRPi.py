import subprocess

def get_ip_and_domain():
    ip_address = subprocess.check_output("hostname -I | awk '{print $1}'", shell=True).decode().strip()
    domain_name = subprocess.check_output("hostname --fqdn", shell=True).decode().strip()
    #return ip_address
    return domain_name, ip_address

#ip = get_ip_and_domain()
domain, ip = get_ip_and_domain()
print("Domain Name:", domain)
print("IP Address:", ip)

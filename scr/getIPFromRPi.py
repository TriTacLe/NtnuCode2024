import subprocess

def get_ip_and_domain_from_pi(pi_user, pi_ip):
    # SSH command to retrieve IP address and hostname
    ip_command = f"ssh {pi_user}@{pi_ip} hostname -I | awk '{{print $1}}'"
    domain_command = f"ssh {pi_user}@{pi_ip} hostname --fqdn"
    
    try:
        ip_address = subprocess.check_output(ip_command, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        ip_address = "Unable to retrieve IP"
        
    try:
        domain_name = subprocess.check_output(domain_command, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        domain_name = "Unable to retrieve domain name"
    
    return domain_name, ip_address

# Replace 'pi' with your Raspberry Pi's username and '<raspberry_pi_ip_address>' with its IP
domain, ip = get_ip_and_domain_from_pi('gruppe12.local', '192.168.1.133')
print("Domain Name:", domain)
print("IP Address:", ip)

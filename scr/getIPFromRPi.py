import subprocess

def get_ip_and_domain_from_pi(pi_user, pi_ip):
    # SSH commands to retrieve IP address, hostname, and model info
    ip_command = f"hostname -I | awk '{{print $1}}'"
    domain_command = f"hostname --fqdn"
    model_command = f"cat /proc/cpuinfo | grep 'Model'"

    try:
        ip_address = subprocess.check_output(ip_command, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        ip_address = "Unable to retrieve IP"

    try:
        domain_name = subprocess.check_output(domain_command, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        domain_name = "Unable to retrieve domain name"

    try:
        #his command checks for 'Raspberry Pi' in the model name, which is unique to Pi devices
        model_info = subprocess.check_output(model_command, shell=True).decode().strip()
        if 'Raspberry Pi' in model_info:
            is_raspberry_pi = True
        else:
            is_raspberry_pi = False
    except subprocess.CalledProcessError:
        model_info = "Unable to retrieve model information"
        is_raspberry_pi = False
    
    return domain_name, ip_address, is_raspberry_pi

# Example usage
domain, ip, is_raspberry_pi = get_ip_and_domain_from_pi('enmo', '192.168.1.133')
print("Domain Name:", domain)
print("IP Address:", ip)
print("Is Raspberry Pi:", is_raspberry_pi)
import subprocess

# Ping to all host in the network
# Using fping packet to perform fast ping
# for i in range(1, 255):
#     subprocess.check_output(("fping", "-t50", "192.168.1.%d" %i))

# Find ip from MAC address
def find_ip(mac_address):
    # Get the list of IP and MAC address in the network
    list_ip = subprocess.check_output(("arp", "-a"))
    list_ip = list_ip.decode("utf-8")
    list_ip = list_ip.splitlines()
    # Find IP of camera
    for line in list_ip:
        if line.find(mac_address) != -1:
            # extract the ip address
            ip_address = line[line.find("(")+1:line.find(")")]
    return ip_address
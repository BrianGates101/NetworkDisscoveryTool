import nmap
import time

def discover_devices(network, retries=3, delay=5):
    nm = nmap.PortScanner()
    devices = []

    for attempt in range(retries):
        nm.scan(hosts=network, arguments='-sP -PR')
        for host in nm.all_hosts():
            # print(f"Debug: Host {host} data: {nm[host]}")  # Debug statement to print host data
            ip_address = nm[host]['addresses'].get('ipv4', '')
            mac_address = nm[host]['addresses'].get('mac', '')
            vendor = nm[host]['vendor'].get(mac_address, '')
            host_name = nm[host]['hostnames'][0]['name'] if nm[host]['hostnames'] != '' else ''
            
            devices.append({
                'ip': ip_address,
                'mac': mac_address,
                'vendor': vendor,
                'host_name': host_name
            })
        time.sleep(delay)  # Wait before the next scan attempt

    # Remove duplicates based on IP address
    unique_devices = {device['ip']: device for device in devices}.values()
    return list(unique_devices)
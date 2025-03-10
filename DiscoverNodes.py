import nmap

def discover_devices(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')
    devices = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            devices.append({
                'ip': nm[host]['addresses']['ipv4'],
                'mac': nm[host]['addresses']['mac'],
                'vendor': nm[host]['vendor'].get(nm[host]['addresses']['mac'], 'Unknown')
            })
        else:
            devices.append({
                'ip': nm[host]['addresses']['ipv4'],
                'mac': 'Unknown',
                'vendor': 'Unknown'
            })
    return devices
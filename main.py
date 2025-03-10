import logging
from DiscoverNodes import discover_devices

# Configure logging
logging.basicConfig(filename='errlog.log', level=logging.ERROR)

def ip_key(ip):
    return list(map(int, ip.split('.')))

if __name__ == "__main__":
    try:
        network = '192.168.0.0/24'
        devices = discover_devices(network)
        sorted_devices = sorted(devices, key=lambda device: ip_key(device['ip']))
        for device in sorted_devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
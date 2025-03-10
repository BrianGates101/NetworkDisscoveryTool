import logging
from DiscoverNodes import discover_devices
from tabulate import tabulate

# Configure logging
logging.basicConfig(filename='errlog.log', level=logging.ERROR)

def ip_key(ip):
    return list(map(int, ip.split('.')))

if __name__ == "__main__":
    try:
        network = '192.168.0.0/24'
        devices = discover_devices(network)
        sorted_devices = sorted(devices, key=lambda device: ip_key(device['ip']))
        
        # Prepare data for tabulate
        table_data = []
        for device in sorted_devices:
            table_data.append([device['ip'], device['mac'], device['vendor'], device['host_name']])
        
        # Define table headers
        headers = ["IP Address", "MAC Address", "Vendor", "Host Name"]
        
        # Print the table
        print(tabulate(table_data, headers, tablefmt="grid"))
        
        print(f"Total devices discovered: {len(devices)}")
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
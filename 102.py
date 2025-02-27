import sys
import scapy.all as scapy

def main():
    """Main function to perform ARP spoofing on the specified network range."""
    if len(sys.argv) != 3:
        print("Usage: python script.py <interface> <ip_range>")
        return
    
    interface = sys.argv[1]
    ip_range = sys.argv[2]
    
    # Scan the network
    try:
        print(f"Scanning network: {ip_range} on interface: {interface}")
        network_info = arp_scan(interface, ip_range)
    except Exception as e:
        print(f"Network scanning failed: {e}")
        return

    # Get gateway information
    try:
        gateway_info_from_scan = gateway_info(network_info)
        if gateway_info_from_scan == "invalid network definition":
            print("You have specified an invalid network definition.")
            return
    except Exception as e:
        print(f"Error in determining gateway info: {e}")
        return

    print(f"Gateway info: {gateway_info_from_scan}")

    # Attempt to swap the ARP table
    try:
        gateway_info_to_swapp = gateway_info_from_scan
        swap_arp_table(gateway_info_to_swapp)
        print("ARP table swapped successfully!")
    except Exception as error:
        print(f"Something went wrong when swapping the ARP table: {error}")

if __name__ == "__main__":
    print("Network scanner and ARP table swapper.")
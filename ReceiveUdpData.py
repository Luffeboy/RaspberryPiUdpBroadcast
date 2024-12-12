import socket

#UDP_IP = '<broadcast>'
UDP_IP = '0.0.0.0' # Broadcast address, usually 255.255.255.255 or fixed LAN address
UDP_PORT = 5005 # broadcast port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((UDP_IP, UDP_PORT))

print("listening...")
while True:
    data, addr = sock.recvfrom(1024)
    print("Received message: ", data)
import socket
from ip_header import ip_header_x
from tcp_header import tcp_header_x
from ether_header import ether_header_x


IFACE = 'virbr3'

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind((IFACE, 0))

# Headers in HEX format. Long form b'/x45/x00/x...' 
#print(ether_header_x, ip_header_x, tcp_header_x)
packet = bytes.fromhex("".join(ether_header_x) + "".join(ip_header_x) + "".join(tcp_header_x))
print(packet, len(packet))
s.send(packet)


import socket

TARGET_IP = '192.168.10.2'

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind(("virbr3", 0))

# Headers in HEX format. Long form b'/x45/x00/x...' 
ether_header = '525400a2c384525400ba86af0800'
ip_header = '4500003cfbd440004006a993c0a80a01c0a80a02'

packet = bytes.fromhex(ether_header + ip_header)
s.send(packet)


from hex_functions import header_hex
from checksum_calculator import calculate_checksum
from dns_message import dns_header_x

### UDP Header ###

payload_len = 29
payload = dns_header_x

udp_header = {
    "src_port": 36201,
    'dst_port': 53,
    "len": 8, # bytes
    "checksum": 0,
    "data": ""
}

u_data_len = len(udp_header["data"].encode().hex()) // 2
udp_header['len'] += payload_len

pseudo_header = {
    'ip_src': '192.168.10.1',
    'ip_dst': '192.168.10.2',
    'rsrvd': 0,
    'proto': 17,
    'len': udp_header["len"]
}

udp_header_x = header_hex(udp_header, 'XX', 'XX', 'XX', 'XX', 'N')
udp_header_x.append(payload)

pseudo_header_x = header_hex(pseudo_header, 'XXXX_IP', 'XXXX_IP', 'X', 'X', 'XX')
u_checksum = calculate_checksum(bytes.fromhex("".join(pseudo_header_x) + "".join(udp_header_x)))
udp_header_x[3] = f"{u_checksum:02x}"

print(udp_header_x, udp_header["len"], "pseudo_len: ", pseudo_header["len"])

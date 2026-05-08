from hex_functions import header_hex
from checksum_calculator import calculate_checksum
from dns_message import dns_header_x
from addresses import ip_src, ip_dst

### UDP Header ###

#payload = "7b8b0100000100000000000007796f757475626503636f6d0000010001"
payload = dns_header_x
payload_len = len(payload) // 2 # 29 DNS

udp_header = {
    "src_port": 36202,
    'dst_port': 53,
    "len": 8, # bytes
    "checksum": 0,
    "data": ""
}

u_data_len = len(udp_header["data"].encode().hex()) // 2
udp_header['len'] += payload_len

pseudo_header = {
    'ip_src': ip_src,
    'ip_dst': ip_dst,
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
print("Payload: ", payload, "Payload len", payload_len)

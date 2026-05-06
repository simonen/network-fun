from hex_functions import header_hex
from checksum_calculator import calculate_checksum

### UDP Header ###

udp_header = {
    "src_port": 36201,
    'dst_port': 12345,
    "len": 8, # bytes
    "checksum": 0,
    "data": "Hello"
}

u_data_len = len(udp_header["data"].encode().hex()) // 2
udp_header['len'] += u_data_len

pseudo_header = {
    'ip_src': '192.168.10.1',
    'ip_dst': '192.168.10.2',
    'rsrvd': 0,
    'proto': 17,
    'len': 13
}

udp_header_x = header_hex(udp_header, 'BB', 'BB', 'BB', 'BB', 'S')
pseudo_header_x = header_hex(pseudo_header, 'BBBB_IP', 'BBBB_IP', 'B', 'B', 'BB')
u_checksum = calculate_checksum(bytes.fromhex("".join(pseudo_header_x) + "".join(udp_header_x)))
udp_header_x[3] = f"{u_checksum:02x}"

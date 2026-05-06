from hex_functions import BB, S, hexify, BBBBIP, B
from checksum_calculator import calculate_checksum

### UDP Header ###

udp_header = {
    "src_port": 36201,
    'dst_port': 12345,
    "len": 8, # bytes
    "checksum": 0,
    "data": "Hello"
}

u_data_len = len(S(udp_header['data'])) // 2
udp_header['len'] += u_data_len

pseudo_header = {
    'ip_src': '192.168.10.1',
    'ip_dst': '192.168.10.2',
    'rsrvd': 0,
    'proto': 17,
    'len': udp_header['len']
}


hex_funcs = [BB, BB, BB, BB, S]
udp_header_x = hexify(hex_funcs, udp_header)
pseudo_funcs = [BBBBIP, BBBBIP, B, B, BB]
pseudo_header_x = hexify(pseudo_funcs, pseudo_header)
u_checksum = calculate_checksum(bytes.fromhex("".join(pseudo_header_x) + "".join(udp_header_x)))
udp_header_x[3] = BB(u_checksum)

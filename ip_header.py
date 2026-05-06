from checksum_calculator import calculate_checksum
from hex_functions import header_hex


### IPv4 HEADER ###

# [ flags ][ fragment offset ]
#   3 bits    13 bits

ip_flags = {
    "DF": 0b010,
    "MF": 0b001,
    }

ip_proto = {
    'ICMP': 1,
    'TCP': 6,
    'UDP': 17,
}

### IP HEADER ###

tcp_len = 20
udp_len = 13
transport_segment_len = tcp_len
ip_options = []
opt_len = 0 # Must be padded to multiple of 4 bytes
padding = 0 #

ip_header = {
    "ip_ver": 4,
    "ip_ihl": 5,
    "ip_ver_ihl": (4 << 4) + 5,
    "ip_tos": 0,
    "ip_len": 20 + transport_segment_len + opt_len,
    "ip_id": 64468,
    "ip_flags": ip_flags["DF"],
    "ip_frag_offset": 0,
    "ip_flags_foffset": (0b010 << 13) | 0,
    "ip_ttl": 64,
    "ip_proto": ip_proto['TCP'],
    "ip_checksum": 0,
    "ip_src": "192.168.10.1",
    "ip_dst": "192.168.10.2",
    }

ip_header_x = header_hex(ip_header, 'N', 'N', 'B', 'B', 'BB', 'BB', 'N', 'N', 'BB', 'B', 'B', 'BB', 'BBBB_IP', 'BBBB_IP')
ip_checksum = calculate_checksum(bytes.fromhex("".join(ip_header_x)))
# print(ip_header_x)

ip_header_x[7] = f"{ip_checksum:04x}"
# print(ip_header_x)
# print("".join(ip_header_x))


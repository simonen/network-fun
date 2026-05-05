from checksum_calculator import calculate_checksum
from hex_functions import N, B, BB, BBBBIP, hexify


### IPv4 HEADER ###

# [ flags ][ fragment offset ]
#   3 bits    13 bits

ip_flags = {
    "DF": 0b010,
    "MF": 0b001,
    }

### IP HEADER ###

tcp_len = 20
ip_options = []
opt_len = 0 # Must be padded to multiple of 4 bytes
padding = 0 #

header = {
    "ip_ver": 4,
    "ip_ihl": 5,
    "ip_ver_ihl": (4 << 4) + 5,
    "ip_tos": 0,
    "ip_len": 20 + tcp_len + opt_len,
    "ip_id": 64468,
    "ip_flags": ip_flags["DF"],
    "ip_frag_offset": 0,
    "ip_flags_foffset": (0b010 << 13) | 0,
    "ip_ttl": 64,
    "ip_proto": 6,
    "ip_checksum": 0,
    "ip_src": "192.168.10.1",
    "ip_dst": "192.168.10.2",
    }

hex_funcs = [N, N, B, B, BB, BB, N, N, BB, B, B, BB, BBBBIP, BBBBIP]
ip_header_x = hexify(hex_funcs, header)
ip_checksum = calculate_checksum(bytes.fromhex("".join(ip_header_x)))
ip_header_x[7] = f"{ip_checksum:04x}"

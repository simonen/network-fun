from checksum_calculator import calculate_checksum
from hex_functions import header_hex
from addresses import ip_src, ip_dst, src_port, dst_port

### TCP Header ###

tcp_options = "020405b40402080aa2a05455000000000103030a"
tcp_opts_len = len(tcp_options) // 2
# [ Data Offset ][ Reserved + Flags ]
#       4 bits          12 bits
words = (20 + tcp_opts_len) // 4
doff_rsrvd_flags = words << 12

# IP Pseudo-header
pseudo_header = {
    'ip_src': ip_src,
    'ip_dst': ip_dst,
    'reserved': 0,
    'proto': 6,
    'tcp_len': 20 + tcp_opts_len, # Header only
    }


pseudo_header_x = header_hex(pseudo_header, "XXXX_IP", "XXXX_IP", "X", "X", "XX")

tcp_header = {
    'src_port': src_port,
    'dst_port': dst_port,
    'seq_num': 1914382070,
    'ack_num': 0,
    'doffset': 0,
    'rsrvd': 0,
    'flags': ['SYN'],
    'doff_rsrvd_flags': 0,
    'window': 64240,
    'checksum': 0,
    'urg_ptr': 0,
    }

tcp_flags = {
    'CWR': 0b10000000,
    'ECN': 0b01000000,
    'URG': 0b00100000,
    'ACK': 0b00010000,
    'PSH': 0b00001000,
    'RST': 0b00000100,
    'SYN': 0b00000010,
    'FIN': 0b00000001,
    }


for i in tcp_header['flags']:
    doff_rsrvd_flags |= tcp_flags[i]

tcp_header['doff_rsrvd_flags'] = doff_rsrvd_flags
tcp_header['doffset'] = words

tcp_header_x = header_hex(tcp_header, 'XX', 'XX', 'XXXX', 'XXXX', 'N', 'N', 'N', 'XX', 'XX', 'XX', 'XX')
tcp_header_x.append(tcp_options)
tcp_checksum = calculate_checksum(bytes.fromhex("".join(pseudo_header_x) + "".join(tcp_header_x)))
tcp_header_x[6] = f"{tcp_checksum:04x}"

print("TCP Header: ", "".join(tcp_header_x))


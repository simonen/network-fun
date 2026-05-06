from checksum_calculator import calculate_checksum
from hex_functions import header_hex

### TCP Header ###

#tcp_options = {}
tcp_opts_len = 0
# [ Data Offset ][ Reserved + Flags ]
#       4 bits          12 bits
words = (20 + tcp_opts_len) // 4
doff_rsrvd_flags = words << 12

# IP Pseudo-header
pseudo_header = {
    'ip_src': "192.168.10.1",
    'ip_dst': "192.168.10.2",
    'reserved': 0,
    'proto': 6,
    'tcp_len': 20, # Header only
    }

pseudo_header_x = header_hex(pseudo_header, "BBBB_IP", "BBBB_IP", "B", "B", "BB")

tcp_header = {
    'src_port': 80,
    'dst_port': 45871,
    'seq_num': 0,
    'ack_num': 1921828432,
    'doffset': 0,
    'rsrvd': 0,
    'flags': ['RST', 'ACK'],
    'doff_rsrvd_flags': 0,
    'window': 0,
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

tcp_header_x = header_hex(tcp_header, 'BB', 'BB', 'BBBB', 'BBBB', 'N', 'N', 'N', 'BB', 'BB', 'BB', 'BB')

tcp_checksum = calculate_checksum(bytes.fromhex("".join(pseudo_header_x) + "".join(tcp_header_x)))
tcp_header_x[6] = f"{tcp_checksum:04x}"

#print("".join(tcp_header_x))


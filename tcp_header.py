from checksum_calculator import calculate_checksum

def hexify(ip_addr: list):
    ip_hex = [f"{int(octet):02x}" for octet in ip_addr.split(".")]
    return ip_hex

### TCP Header ###
tcp_src_port = 45870
tcp_dst_port = 22
tcp_seq = 1921828437
tcp_ack = 0
#tcp_options = {}
tcp_reserved = 0b0000
tcp_flags = {
            'CWR': 0b10000000,
            'ECN': 0b01000000,
            'URG': 0b00100000,
            'ACK': 0b00010000,
            'PSH': 0b00001000,
            'RST': 0b00000100,
            'SYN': 0b00000010,
            'FIN': 0b00000001,}

# [ Data Offset ][ Reserved + Flags ]. Field bits concatenated.
#       4 bits          12 bits

tcp_header_len = 0b0101 # Header only. 5 x 4 = 20 bytes
flags = tcp_flags['RST']
tcp_window = 0
tcp_urg_pointer = 0
doffset_rsrvd_flgs = (tcp_header_len << 12) | tcp_flags['RST']
tcp_checksum = 0

# IP Pseudo-header
ip_src = "192.168.10.1"
ip_dst = "192.168.10.2"
reserved = "00"
proto = 6
tcp_len = 20 # Header only

pseudo_header = "".join(hexify(ip_src)) + "".join(hexify(ip_dst)) + f"{0:02x}" + f"{proto:02x}" + f"{tcp_len:04x}"

tcp_header = [
    f"{tcp_src_port:04x}", f"{tcp_dst_port:04x}",
    f"{tcp_seq:08x}",
    f"{tcp_ack:08x}",
    f"{doffset_rsrvd_flgs:04x}", f"{tcp_window:04x}",
    f"{tcp_checksum:04x}", f"{tcp_urg_pointer:04x}",
    ]

tcp_checksum = calculate_checksum(bytes.fromhex(pseudo_header + "".join(tcp_header)))
tcp_header[6] = f"{tcp_checksum:04x}"

print(tcp_header)


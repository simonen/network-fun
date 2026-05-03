from checksum_calculator import calculate_checksum


def hexify(ip_addr: list):
    ip_hex = [f"{int(octet):02x}" for octet in ip_addr]
    return ip_hex

### IPv4 HEADER ###
# x = 4
ip_ver_ihl = "0100" + "0101"
ip_tos = 0
ip_id = 64468  # 16 bits
# [ flags ][ fragment offset ]
#   3 bits    13 bits
ip_flags = {
    "DF": 0b010,
    "MF": 0b001,
    }
ip_f_offset = 0b0000000000000
ip_flags_offset = (ip_flags['DF'] << 13) | ip_f_offset
ip_ttl = 64  # 8 bits
ip_proto = 6  # TCP
ip_src = "192.168.10.1".split(".")
ip_dst = "192.168.10.2".split(".")
ip_checksum = "0000"
tcp_seg_len = 20 # header only
ip_len = 20 + tcp_seg_len  # ip header 20 + payload (tcp segment)

ip_header = [
    f"{int(ip_ver_ihl, 2):02x}", f"{ip_tos:02x}", f"{ip_len:04x}",
    f"{ip_id:04x}", f"{ip_flags_offset:04x}",
    f"{ip_ttl:02x}", f"{ip_proto:02x}", ip_checksum,
    "".join(hexify(ip_src)), "".join(hexify(ip_dst))
    ]

for i in range(0, len("".join(ip_header)), 2):
    print("".join(ip_header)[i: i + 2], end=" ")

print()

ip_checksum = calculate_checksum(bytes.fromhex("".join(ip_header)))
ip_header[7] = f"{ip_checksum:04x}"

print("IP Checksum: ", f"{ip_checksum:04x}")
print(ip_header)

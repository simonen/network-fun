def B(field) -> str:
    return f"{field:02x}"


def BB(field):
    return f"{field:04x}"


def BBBB(field):
    return f"{field:08x}"


def N(field):
    return ""


def BBBBIP(field: str):
    return "".join([f"{int(octet):02x}" for octet in field.split(".")])


def ip_header_hex(header: dict) -> list:
    conv_matrix = {
        "ip_ver": lambda x: f"{x:04b}",
        "ip_ihl": lambda x: f"{x:08b}",
        "ip_ver_ihl": lambda x: f"{x:02x}",
        "ip_tos": lambda x: f"{x:02x}",
        "ip_len": lambda x: f"{x:04x}",
        "ip_id": lambda x: f"{x:04x}",
        "ip_flags": lambda x: f"{x:03b}",
        "ip_frag_offset": lambda x: f"{x:013b}",
        "ip_flags_foffset": lambda x: f"{x:04x}",
        "ip_ttl": lambda x: f"{x:02x}",
        "ip_proto": lambda x: f"{x:02x}",
        "ip_checksum": lambda x: f"{x:04x}",
        "ip_src": lambda x: "".join([f"{int(octet):02x}" for octet in x.split(".")]),
        "ip_dst": lambda x: "".join([f"{int(octet):02x}" for octet in x.split(".")]),
        }

    header_done = []
    excluded = ['ip_ver', 'ip_ihl', 'ip_flags', 'ip_frag_offset']

    for k, v in header.items():
        # print(f"{k}: ", conv_matrix[k](header[k]))
        if k not in excluded:
            header_done.append(conv_matrix[k](header[k]))

    return header_done


def hexify(functions: list, header: dict) -> list:
    tcp_header_x = []
    for i in range(len(functions)):
        if functions[i] is N:
            continue
        for v in list(header.values())[i:]:
            tcp_header_x.append(functions[i](v))
            break

    return tcp_header_x

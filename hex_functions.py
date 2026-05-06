def header_hex(header: dict, *args) -> list:
    result = []
    conv_matrix = {
        "BB": lambda x: f"{x:04x}",
        "BBBB": lambda x: f"{x:08x}",
        "B": lambda x: f"{x:02x}",
        "BBBB_IP": lambda x: "".join([f"{int(octet):02x}" for octet in x.split(".")]),
        "S": lambda x: x.encode().hex(),
    }

    index = 0
    for v in header.values():
        for arg in args[index:]:
            index += 1
            if arg == 'N':
                break

            result.append(conv_matrix[arg](v))
            break

    return result

def header_hex(header: dict, *args) -> list:
    result = []
    conv_matrix = {
        "XX": lambda x: f"{x:04x}",
        "XXXX": lambda x: f"{x:08x}",
        "X": lambda x: f"{x:02x}",
        "XXXX_IP": lambda x: "".join([f"{int(octet):02x}" for octet in x.split(".")]),
        "XS": lambda x: x.encode().hex(),
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

def bin_conv(header: list, *args) -> list:
    result = []
    conv_matrix = {
        "B": lambda x: f"{x:01b}",
        "BBB": lambda x: f"{x:03b}",
        "BBBB": lambda x: f"{x:04b}",
    }

    for i in range(len(args)):
        if args[i] == 'N':
            continue

        result.append(conv_matrix[args[i]](header[i]))

    return result


def hex_conv(header: list, *args) -> list:
    result = []
    conv_matrix = {
        "XX": lambda x: f"{x:04x}",
        "XXXX": lambda x: f"{x:08x}",
        "X": lambda x: f"{x:02x}",
        "XXXX_IP": lambda x: "".join([f"{int(octet):02x}" for octet in x.split(".")]),
        "XS": lambda x: x.encode().hex(),
    }

    for i in range(len(args)):
        if args[i] == 'N':
            continue

        result.append(conv_matrix[args[i]](header[i]))

    return result


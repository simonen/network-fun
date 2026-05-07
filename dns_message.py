from hex_functions import header_hex, bin_conv, hex_conv

bin_matrix = ['B', 'BBBB', 'B', 'B', 'B', 'B', 'BBB', 'BBBB']

dns_id = 31627
dns_qr = 0
dns_opcode = 0
dns_aa = 0
dns_tc = 0
dns_rd = 1
dns_ra = 0
dns_z = 0
dns_rcode = 0

flags = [dns_qr, dns_opcode, dns_aa, dns_tc, dns_rd, dns_ra, dns_z, dns_rcode]
bin_flags = bin_conv(flags, *bin_matrix)


# COUNTS
counts = {
    'dns_qdcnt': 1,
    'dns_ancnt': 0,
    'dns_nscnt': 0,
    'dns_arcnt': 0,
    }

count_matrix = ['XX', 'XX', 'XX', 'XX']
count_x = header_hex(counts, *count_matrix)
print(bin_flags)
dns_flagz = f"{int("".join(bin_flags), 2):04x}"
print("flagz ", dns_flagz)
print(count_x)

host = '4ugunis.tan.'.split(".")
query = []
for label in host:
    query.append(len(label))
    query.append(label)

print(query)

q_matrix = ['X', 'XS', 'X', 'XS', 'X', 'N']
query_x = hex_conv(query, *q_matrix)

print(query_x)
print("".join(query_x))

dns_qtype = "0001"
dns_class = "0001"

dns_header_x = f"{dns_id:04x}" + dns_flagz + ''.join(count_x) + "".join(query_x) + dns_qtype + dns_class
print(dns_header_x)


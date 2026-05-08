eno1 = 'c4346b7cb564'
virbr2 = "525400fd5a73"
f_eth0 = '525400ee1102'
broad = 'ffffffffffff'
dst_mac = virbr2
src_mac = f_eth0
ether_type = "0800"

ether_header_x = dst_mac + src_mac + ether_type
#print(ether_header_x)

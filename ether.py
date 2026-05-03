import struct

# Build frame manually
dst = bytes.fromhex('525400a2c384')
src = bytes.fromhex('525400ba86af')
ethertype = struct.pack('>H', 0x0800)  # big-endian
payload = b'Your data here...'  # must be 46-1500 bytes

# Pad if needed
if len(payload) < 46:
    payload += b'\x00' * (46 - len(payload))

frame = dst + src + ethertype + payload
# FCS added by NIC when sending via raw socket

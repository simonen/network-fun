def calculate_checksum(data) -> int:
    """Calculate 16-bit ones' complement checksum"""
    # Ensure even length
    if len(data) % 2 == 1:
        data += b'\x00'

    total = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        total += word
        # Handle carry (ones' complement addition)
        total = (total & 0xffff) + (total >> 16)

    return (~total) & 0xffff

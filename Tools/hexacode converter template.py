# List of hex codes
hex_codes = [
    0x155cbf1, 0x1e4d1b6, 0x17b0b68, 0x1eac9cd, 0x12e14ce, 0x3548bb, 
    0x7757e6, 0x1065dab, 0x1baa2e7, 0xdea688, 0x81d927, 0x51b241, 
    0xdbc8ae, 0x1e50e19, 0x15819d2, 0x16d8282, 0x163e035, 0x9d9b81, 
    0x173eec4, 0xae3a09, 0x5f7c51, 0x1a137fc, 0xdc9562, 0x1802e45, 
    0x1c3542c, 0x870fa4, 0x914709, 0x16684f0, 0xc8f2a5, 0x833ebb, 
    0x59717f, 0x13cd050, 0xfa0ad1, 0x1b763b0, 0xb991ce
]


# Function to convert hex to binary and print
def hex_to_binary(hex_codes):
    i = 0
    for hex_code in hex_codes:
        binary_code = bin(hex_code)[2:].zfill(64)  # Remove '0b' and pad with leading zeros
        last_36_digits = binary_code[-25:]  # Isolate the last 36 digits
        int_list = [int(digit) for digit in last_36_digits]  # Convert to list of integers
        print(f"{i}: {int_list},")
        i += 1

# Call the function to convert and print the binary data
hex_to_binary(hex_codes)

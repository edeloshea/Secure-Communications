hex_str = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

bytes_obj = bytes.fromhex(hex_str)

ascii_str = bytes_obj.decode("ASCII")

print(ascii_str)
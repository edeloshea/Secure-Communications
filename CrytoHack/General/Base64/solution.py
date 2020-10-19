import base64
from binascii import unhexlify

hex_str = unhexlify('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
base64_bytes = base64.b64encode(hex_str)
print(base64_bytes)
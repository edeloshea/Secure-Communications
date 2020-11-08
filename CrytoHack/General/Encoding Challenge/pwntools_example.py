from pwn import * # pip install pwntools
import json

from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from binascii import unhexlify

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(0,101):
    received = json_recv()
    if "flag" in received:
        print(received["flag"])
        break

    encoded = received["encoded"]
    
    encType = received["type"]

    if encType == "base64":
        decoded = base64.b64decode(encoded).decode('utf8').replace("'", '"')
    elif encType == "hex":
        decoded = (unhexlify(encoded)).decode('utf8').replace("'", '"')
    elif encType == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif encType == "bigint":
        decoded = unhexlify(encoded.replace("0x", "")).decode('utf8').replace("'", '"')
    elif encType == "utf-8":
        decoded = ""
        decoded = decoded.join([chr(b) for b in encoded])

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)
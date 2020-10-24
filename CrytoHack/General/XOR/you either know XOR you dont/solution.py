def brute(input, key):
    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "error"

msg = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(msg)

partial = brute(msg[:7], "crypto{".encode())
print(partial)

key = (partial + "y").encode()
print(key)

int1 = int((len(msg) - len(key))/len(key))
key += key * int1
int2 = (len(msg) - len(key))%len(key)
key += key[:int2]

print(key)

flag = brute(msg, key)

print(flag)
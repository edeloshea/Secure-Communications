"""
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x5dead6954f77c98a"}
Intercepted from Bob: {"B": "0xa3ede823ca02081e"}
Intercepted from Alice: {"iv": "876722524a10d12298becfc71416ac33", "encrypted_flag": "b29fc3a29e461dd6349e2befd6fa3a4704555140bafe0045802ec4c30526d711"}
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


p = 0xde26ab651b92a129
g = 0x2
A = 0x5dead6954f77c98a
B = 0xa3ede823ca02081e
iv = '876722524a10d12298becfc71416ac33'
encrypted_flag = 'b29fc3a29e461dd6349e2befd6fa3a4704555140bafe0045802ec4c30526d711'

from sympy.ntheory import discrete_log

p = int('0xde26ab651b92a129',0)
g = int('0x2',0)
A = int('0x5dead6954f77c98a',0)
B = int('0xa3ede823ca02081e',0)
#a = (discrete_log(A,g,p))
#a = discrete_log(p,g,A)
a = discrete_log(p,A,g)
print (a)

a = 3239405777878271371
shared = pow(B,a,p)
print(decrypt_flag(shared, iv, encrypted_flag))

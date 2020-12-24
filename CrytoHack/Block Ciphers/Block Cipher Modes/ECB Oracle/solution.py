from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests


url = 'http://aes.cryptohack.org/'
encrypt = '/ecb_oracle/encrypt/'

## flag is the element added to the plaintext before encryption
a = "aa"
b = a.encode('utf-8')
c = b.hex()
print (b.hex())


s = requests.get(url+encrypt+str(c))

data2 = s.json()

ciphertext = data2['ciphertext']

print (ciphertext)

## encrypted flag
##4ce34d0ad3020e6fb718f949c20907b5

## f720f5b9f20edd4ff416fe129b8b1acc12782223d20e22e6ec1ff9f401f9facc
## a036fd893c58d05958c4067b8db5a4a912782223d20e22e6ec1ff9f401f9facc
## 9e11ea091fe6de88a865418693c882f1ce5d24d7da994b2a8bfc7167a9c29c1b

"""
KEY = ?
FLAG = ?

@chal.route('/ecb_oracle/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}
"""
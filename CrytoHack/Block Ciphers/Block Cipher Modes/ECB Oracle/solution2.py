import requests

url = 'http://aes.cryptohack.org/'
encrypt = '/ecb_oracle/encrypt/'
decrypt = '/block_cipher_starter/decrypt/'

#get the encryted flag from the website
r = requests.get(url+encrypt)

data = r.json()
ciphertext = data['ciphertext']

print(ciphertext)

"""
#get the decrypted flag from the website
r = requests.get(url+decrypt+ciphertext)

data = r.json()
plaintext = data['plaintext']

print(bytes.fromhex(plaintext))
"""

"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


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
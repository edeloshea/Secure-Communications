from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad, unpad
import requests

url = 'http://aes.cryptohack.org/'
encrypt = 'ecbcbcwtf/encrypt_flag/'
decrypt = 'ecbcbcwtf/decrypt/'

r = requests.get(url+encrypt)

data = r.json()
ciphertext = data['ciphertext']

print(ciphertext)

#get the decrypted flag from the website
r = requests.get(url+decrypt+ciphertext)

data = r.json()
plaintext = data['plaintext']

print (plaintext)

print(bytes.fromhex(plaintext))


"""
from string import printable
print (printable)

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '00000000000000000000000000000000000000000000000000000000000000'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = 'a212eee031'
    if j in str(ciphertext):
        print (a)
        print (d)


from Crypto.Cipher import AES


KEY = ?
FLAG = ?
"""
"""

@chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}

"""
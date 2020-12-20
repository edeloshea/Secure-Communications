import requests
from Crypto.Cipher import AES
import hashlib
import random

url = 'http://aes.cryptohack.org/'
encrypt = '/passwords_as_keys/encrypt_flag/'
decrypt = '/passwords_as_keys/decrypt/'

r = requests.get(url+encrypt)

data = r.json()

cipher = data['ciphertext']

print(cipher)


with open("/home/b00139077/college/Secure-Communications/CrytoHack/Block Ciphers/Block Cipher Modes/Passwords as Keys/words.txt") as f:
   words = [w.strip() for w in f.readlines()]

for  word in words:
   m = hashlib.md5()
   m.update(word.encode())
   k = m.hexdigest()
   
   s = requests.get(url+decrypt+cipher+'/'+str(k))

   data2 = s.json()

   plain = data2['plaintext']

   plaintext = bytearray.fromhex(data2['plaintext'])
   
   if "crypt" in str(plain):
      print (plain)
   
   if "crypt" in str(plaintext):
      print (plaintext)


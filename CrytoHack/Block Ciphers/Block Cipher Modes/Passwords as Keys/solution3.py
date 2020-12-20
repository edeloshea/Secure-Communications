#f = open("/home/b00139077/college/Secure-Communications/CrytoHack/Block Ciphers/Block Cipher Modes/Passwords as Keys/words.txt", "r")
#print(f.read()) 

import requests
from Crypto.Cipher import AES
import hashlib
import random

with open("/home/b00139077/college/Secure-Communications/CrytoHack/Block Ciphers/Block Cipher Modes/Passwords as Keys/words.txt") as f:
   words = [w.strip() for w in f.readlines()]
   print (words)
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
print (KEY)
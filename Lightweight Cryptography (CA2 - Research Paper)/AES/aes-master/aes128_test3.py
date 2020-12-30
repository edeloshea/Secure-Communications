# uses aes.py
import aes, os

key = os.urandom(16)
iv = os.urandom(16)

## Encryption
print ("ENCRYPTION")
print ("Same plaintext, key and iv")
for i in range (1,6):
    encrypted = aes.AES(key).encrypt_ctr(b'Edel Edel Edel', iv)
    print ("Ciphertext " + str(i) + " is " + str(encrypted))

print ("") 
print("Same plaintext and iv, with different keys")
for i in range (6,11):
    key = os.urandom(16)
    encrypted = aes.AES(key).encrypt_ctr(b'Edel Edel Edel', iv)
    print ("Ciphertext " + str(i) + " is " + str(encrypted))

print ()
print ("Same plaintext and key, with different iv")
for i in range (11,16):
    iv = os.urandom(16)
    encrypted = aes.AES(key).encrypt_ctr(b'Edel Edel Edel', iv)
    print ("Ciphertext " + str(i) + " is " + str(encrypted))


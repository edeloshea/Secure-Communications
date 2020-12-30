# uses aes.py
import time
import aes, os

key = os.urandom(16)
iv = os.urandom(16)

encrypt_total = 0
decrypt_total = 0
    
for i in range (0, 50000):
    encrypt_start = time.time()
    encrypted = aes.AES(key).encrypt_ctr(b'Edel', iv)
    encrypt_time = time.time() - encrypt_start
    encrypt_total += encrypt_time

    decrypt_start = time.time()
    decrypt_start = time.time()
    decrypted = aes.AES(key).decrypt_ctr(encrypted, iv)
    decrypt_time = time.time() - decrypt_start
    decrypt_total += decrypt_time

print ("The total encryption time is " + str(encrypt_total))
print ("The total decryption time is " + str(decrypt_total))


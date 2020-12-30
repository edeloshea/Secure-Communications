# uses aes.py

"""Test the implemetation of AES-128 encryption and decryption"""
print ("Testing the AES-128 crypotgraphic algorithm")
import aes, os

key = os.urandom(16)
iv = os.urandom(16)

print ("'Edel' will be used as the test word for the encryption and decryption. The key and IV used will be randomly generated")
print ("All variables are in bytes. For ease of reading, they will be decoded and displayed as plain string.")
print ("")

print ("The key generated is: " + ((str(key))[2:]))
print ("The iv generated is: " + ((str(iv))[2:]))
print ("")

## Encryption
print ("ENCRYPTION")
print("Now we will encrypt 'Edel' with the key and iv generated")
encrypted = aes.AES(key).encrypt_ctr(b'Edel', iv)
encrypted_decoded = ((str(encrypted))[2:])
print ("The ciphertext is: " + encrypted_decoded)
print ("")

## Decryption
print ("DECRYPTION")
print ("Now we will decrypt the message with the same key and iv")
decrypted = aes.AES(key).decrypt_ctr(encrypted, iv)
decoded_decrypted = decrypted.decode("utf-8")
print("The plaintext is: " + decoded_decrypted)


import requests

url = 'http://aes.cryptohack.org/'
encrypt = '/block_cipher_starter/encrypt_flag/'
decrypt = '/block_cipher_starter/decrypt/'

#get the encryted flag from the website
r = requests.get(url+encrypt)

data = r.json()
ciphertext = data['ciphertext']

print(ciphertext)

#get the decrypted flag from the website
r = requests.get(url+decrypt+ciphertext)

data = r.json()
plaintext = data['plaintext']

print(bytes.fromhex(plaintext))
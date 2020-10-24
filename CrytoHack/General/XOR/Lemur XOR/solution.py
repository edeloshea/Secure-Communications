from PIL import Image, ImageChops
import numpy as np
from pwn import xor

flagimg = Image.open('/home/b00139077/college/Secure-Communications/CrytoHack/General/XOR/Lemur XOR/flag.png').convert('1')
lemurimg = Image.open('/home/b00139077/college/Secure-Communications/CrytoHack/General/XOR/Lemur XOR/lemur.png').convert('1')

key = ''

imgXOR = ImageChops.logical_xor(lemurimg, flagimg)

#output of flagimg = 0x7F9886E85A60
#output of lemurimg = 0x7F9886E80FD0
#output of XOR'd images = 0x7FB926868880

# key2 = xor(bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'), key1)

code1 = bytes.fromhex('7F9886E85A60')

code2 = bytes.fromhex('7F9886E80FD0')

code3 = bytes.fromhex('7FB926868880')

print (code1)
print (code2)
print (code3)

code4 = xor(code3, code2)

print (code4)





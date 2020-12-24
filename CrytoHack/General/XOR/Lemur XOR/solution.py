from PIL import Image, ImageChops
import numpy as np
from pwn import xor

flagimg = Image.open('/home/b00139077/college/Secure-Communications/CrytoHack/General/XOR/Lemur XOR/flag.png').convert('1')
lemurimg = Image.open('/home/b00139077/college/Secure-Communications/CrytoHack/General/XOR/Lemur XOR/lemur.png').convert('1')
result = Image.open('/home/b00139077/college/Secure-Communications/CrytoHack/General/XOR/Lemur XOR/result.png').convert('1')


#imgXOR = ImageChops.logical_xor(lemurimg, flagimg)
#imgXOR.save('result.png')

imgXOR = ImageChops.logical_xor(lemurimg, result)
imgXOR.save('result2.png')

imgXOR2 = ImageChops.logical_xor(flagimg, result)
imgXOR2.save('result3.png')




#output of flagimg = 0x7F9886E85A60
#output of lemurimg = 0x7F9886E80FD0
#output of XOR'd images = 0x7FB926868880

# key2 = xor(bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'), key1)

#C1=  m1⊕PRNG(k) C2=  m2⊕PRNG(k)
#C1⊕C2  =  m1⊕m2





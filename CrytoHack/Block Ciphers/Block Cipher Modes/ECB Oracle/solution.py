from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

## 2 full blocks
# 65f4b06d7f0d63efcac7c5c0ceabbb07ff4e720deb0cd91085e6d354f9e0395e4ce34d0ad3020e6fb718f949c20907b5

## 2 blocks (1byte padding)
# 65f4b06d7f0d63efcac7c5c0ceabbb077ce33026ad76ad67f2baf74d3fa8dd6312782223d20e22e6ec1ff9f401f9facc

## 2 blocks (2bytes padding)
# 65f4b06d7f0d63efcac7c5c0ceabbb073d2ae9f17ccaa40d309a4340a23a292bad92c5d68f8a34d85892535260eb3904

## 2 blocks (3 bytes padding)
# 65f4b06d7f0d63efcac7c5c0ceabbb0779820a9a24e15e3cd56bbf0bf966981c057ddd96c6fbf3382c436adc80ef675e

## 2 blocks (4 bytes of padding)
# 65f4b06d7f0d63efcac7c5c0ceabbb0779820a9a24e15e3cd56bbf0bf966981c057ddd96c6fbf3382c436adc80ef675e

## 2 blocks (5 bytes of padding)
# 65f4b06d7f0d63efcac7c5c0ceabbb0775f5a56861781f503f5a9ea9eb6d0cd0846f380ab5ae93fdd2459edd8b54df2d

## 2 blocks (6 bytes of padding)
# 65f4b06d7f0d63efcac7c5c0ceabbb07d183bddb20d13eeae804fc91aee3940fce5d24d7da994b2a8bfc7167a9c29c1b

## 2 blocks (7 bytes of padding)
# 65f4b06d7f0d63efcac7c5c0ceabbb079c3f5ebd585514acc756009c081c02f8f9d59733f1bfacce87707d5230c3e4fe

##LETTER 1
## 2 blocks (8 bytes of padding) *** Start impacting the first block so first letter is here.
# a212eee0315ccd406292c1b90cdb33a9333fb3b4953a5a512e08e1191b99fd46e5120775c49f225d4af593766f1c76d7

## LETTER 2
# b52587b95dcc1bb31fcc1a4e648eecfb9bb6d2f8c99ab779514e0c881aeaf41c949c35e160a893f10e20e747dea2e1d9

## LETTER 3
# b9ac3eeb9bf34a8ddbd2ed58e7d9962ddbd9ddc2c9c5a1da25ad216c496ee104f8cccba3d6bc3d4abbfb5e03a4f73fff

## LETTER 4
# 8e776aa398bb4c4cfaf15731dddf05f434fc748bcdb1fed1885c0c26612d8cd8e809ad4e98e2a11cc87bac33f3ad575f

## LETTER 5
# 4a22d0f492c00ef9389e474ecc2d6261dd161f19e1b48fa2514f4e5a073cfdac438234e6d566d6acab713331c7192fc4

## LETTER 6
# 6558156e173335ccac36feff4ee67882ad38c8d50e4c5b93fe75c890910aff73aabf618da400ee2aadaf068aaa632f30

## LETTER 7
# bab31733de2f1ab7d34fae791869c34921ee23cace82bc52d5dfdc7c62506b82673990ff75273fe1975f2263d522c6ec

## LETTER 8
# 7f7b576afdca2a509d484e53bd398aeaffe779498cdb968e2bb7aae898af7349fc6910bb84748df7174750d0964593c3

## LETTER 9
# 21bf123d846c7eddfbbbd48a8e3b3939d587a3273b31b6a778c6bfb23e24020bf788b27a7555f3aea210954b0ec88b72

## LETTER 10
# ff4e720deb0cd91085e6d354f9e0395e4ce34d0ad3020e6fb718f949c20907b5

## LETTER 11
# 7ce33026ad76ad67f2baf74d3fa8dd6312782223d20e22e6ec1ff9f401f9facc

## LETTER 12
# 3d2ae9f17ccaa40d309a4340a23a292bad92c5d68f8a34d85892535260eb3904

## LETTER 13
# 79820a9a24e15e3cd56bbf0bf966981c057ddd96c6fbf3382c436adc80ef675e

## LETTER 14
# 75f5a56861781f503f5a9ea9eb6d0cd0846f380ab5ae93fdd2459edd8b54df2d

## LETTER 15
# d183bddb20d13eeae804fc91aee3940fce5d24d7da994b2a8bfc7167a9c29c1b

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

url = 'http://aes.cryptohack.org/'
encrypt = '/ecb_oracle/encrypt/'

from string import printable
print (printable)


for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '000000000000000000000000000000'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = 'a212eee0315ccd406292c1b9'
    if j in str(ciphertext):
        print (a)
    
for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '000000000000000000000000000063'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = 'b52587b95dcc1bb31fcc1a4e'
    if j in str(ciphertext):
        print (a)

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '000000000000000000000000006372'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = 'b9ac3eeb9bf34a8dd'
    if j in str(ciphertext):
        print (a)

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '000000000000000000000000637279'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = '8e776aa398bb4c'
    if j in str(ciphertext):
        print (a)

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '000000000000000063727970746f7b'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = '7f7b576afdca2a509d484e5'
    if j in str(ciphertext):
        print (a)
        print (d)


# p = 70
#crypto{p

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '0000000000000063727970746f7b70'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = '21bf123d846c7eddfbbbd'
    if j in str(ciphertext):
        print (a)
        print (d) 

# 3 = 33
#crypto{p3

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '00000000000063727970746f7b7033'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = 'ff4e720deb0cd91085'
    if j in str(ciphertext):
        print (a)
        print (d) 

# n = 6e
# crypto{p3n}


for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '000000000063727970746f7b70336e'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = '7ce33026ad76ad67f'
    if j in str(ciphertext):
        print (a)
        print (d) 

# 6 = 36
# crypto{p3n6

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '0000000063727970746f7b70336e36'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = '3d2ae9f17ccaa40d'
    if j in str(ciphertext):
        print (a)
        print (d) 

# u = 75
# crypto{p3n6u

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '00000063727970746f7b70336e3675'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = '79820a9a24e15'
    if j in str(ciphertext):
        print (a)
        print (d) 

# 1 = 31
# crypto{p3n6u1

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '000063727970746f7b70336e367531'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
   
    j = '75f5a56861781f503'
    if j in str(ciphertext):
        print (a)
        print (d) 

# n = 6e
# crypto{p3n6u1n

for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '0063727970746f7b70336e3675316e'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
    
    j = 'd183bddb20d13eeae'
    if j in str(ciphertext):
        
        print (ciphertext)
        print (a)
        print (d) 

# 5 = 35
# crypto{p3n6u1n5
"""
for i in printable:
    a = str(i)
    b = a.encode('utf-8')
    c = '63727970746f7b70336e3675316e35'
    d = b.hex()
    e = str(c) + str(d)

    s = requests.get(url+encrypt+e)

    data2 = s.json()

    ciphertext = data2['ciphertext']
    
    j = '4f9e03'
    if j in str(ciphertext):
        
        print (ciphertext)
        print (a)
        print (d) 

"""
## 65f4b06d7f0d63efcac7c5c0ceabbb07ff4e720deb0cd91085e6d354f9e0395e4ce34d0ad3020e6fb718f949c20907b5
## encrypted flag
##4ce34d0ad3020e6fb718f949c20907b5

# e5c31b9d2ae1e9578f764fd0665e48fd34fc748bcdb1fed1885c0c26612d8cd8e809ad4e98e2a11cc87bac33f3ad575f

## f720f5b9f20edd4ff416fe129b8b1acc12782223d20e22e6ec1ff9f401f9facc
## a036fd893c58d05958c4067b8db5a4a912782223d20e22e6ec1ff9f401f9facc
## 9e11ea091fe6de88a865418693c882f1ce5d24d7da994b2a8bfc7167a9c29c1b
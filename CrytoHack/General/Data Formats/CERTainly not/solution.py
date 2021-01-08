"""
import sys
import chilkat

cert = chilkat.CkCert()

#  LoadFromFile will load virtually any certificate format file.
#  It will auto-recognize the format and load appropiately.
#  In this case, load a DER format certificate and convert to PEM.
success = cert.LoadFromFile("/home/b00139077/college/Secure-Communications/CrytoHack/General/Data Formats/CERTainly not/2048b-rsa-example-cert.der")
if (success != True):
    print(cert.lastErrorText())
    sys.exit()

success = cert.ExportCertPemFile("/home/b00139077/college/Secure-Communications/CrytoHack/General/Data Formats/CERTainly not/2048b-rsa-example-cert.pem")
if (success != True):
    print(cert.lastErrorText())
    sys.exit()

print("Converted certificate from DER to PEM format.")
"""
"""
from Crypto.PublicKey import RSA
f = open("/home/b00139077/college/Secure-Communications/CrytoHack/General/Data Formats/CERTainly not/2048b-rsa-example-cert.der", "r")
#text = f.read()
#print (text.decode('UTF-8'))
key = RSA.importKey(f.read())
print (key)
"""
"""
import sys
import chilkat

cert = chilkat.CkCert()

#  LoadFromFile will load virtually any certificate format file.
#  It will auto-recognize the format and load appropiately.
success = cert.LoadFromFile("/home/b00139077/college/Secure-Communications/CrytoHack/General/Data Formats/CERTainly not/2048b-rsa-example-cert.pem")
if (success != True):
    print(cert.lastErrorText())
    sys.exit()

#  DN = "Distinguished Name"
print("SubjectDN:" + cert.subjectDN())

print("Common Name:" + cert.subjectCN())
print("Issuer Common Name:" + cert.issuerCN())

print("Serial Number:" + cert.serialNumber())
"""

from Crypto.PublicKey import RSA

f = open('/home/b00139077/college/Secure-Communications/CrytoHack/General/Data Formats/CERTainly not/2048b-rsa-example-cert.der','r')

key= RSA.importKey(f.read())

print (key.d)


with open("cert.der", "rb") as f:
    der = f.read()
 
import OpenSSL.crypto 
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, der)
pkey = x509.get_pubkey()
dir(pkey)
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'bits', 'check', 'generate_key', 'type']
pkey.bits()
4096L
pkey.type() == OpenSSL.crypto.TYPE_RSA
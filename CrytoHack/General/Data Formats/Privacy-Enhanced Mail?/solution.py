from Crypto.PublicKey import RSA

f = open('/home/b00139077/college/Secure-Communications/CrytoHack/General/Data Formats/Privacy-Enhanced Mail?/privacy_enhanced_mail.pem','r')

key= RSA.importKey(f.read())

print (key.d)

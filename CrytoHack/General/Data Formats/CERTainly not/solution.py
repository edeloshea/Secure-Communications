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
#!/usr/bin/env python3

# --------------- OTP Python code example --------------
########################################################

def string2Int(message):
    return int(message.encode().hex(),16)                   ## remove .encode() if it's already a byte string

def int2String(int_message):
    return bytes.fromhex(hex(int_message)[2:]).decode()

def string2Hex(message):
     return message.encode().hex() 

def hex2String(hex_message):
    return bytes.fromhex(hex_message).decode()     

# Takes 2 hex formated strings and XORs the two strings
# ------------------------------------------------------
def XORStrings(a,b):	
    # convert to integers and xor them		
    result = int(a, 16) ^ int(b, 16) 	
    # return result in hex format
    return '{:x}'.format(result)	


# Takes 2 ascii strings and XORs the two strings
# prints one character per line.. not all XORed strings 
# will be printable, and will appear blank.
# ------------------------------------------------------
def XORStringsByLine(s1,s2):    
    for a,b in zip(s1,s2):
    	print (chr(ord(a) ^ ord(b))) 
    return 1



test = "this is my test message"
test2 = "another random message here"

## As intergers used with RSA etc.
print ('As an integer:')
print ('--------------------------------------------------------')
print (string2Int(test))
print (int2String(string2Int(test)))

## As hex used with OTP and others
print ()
print ('As hex :')
print ('--------------------------------------------------------')
print (string2Hex(test))
print (hex2String(string2Hex(test)))

## XOR messages together

## XOr ascii messages
XORStringsByLine(test,test2)

## As Hex messages
print (XORStrings(string2Hex(test),string2Hex(test2)))
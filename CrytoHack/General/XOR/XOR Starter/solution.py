text = "label"
flag = ''

for i in text:
    flag += chr(ord(i) ^ 13)

flag2 = 'crypto{' + flag + '}'

print(flag2)
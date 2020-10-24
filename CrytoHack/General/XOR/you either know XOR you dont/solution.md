
Define a funciton *sourced from Github (https://captainmich.github.io/programming_language/CTF/Challenge/CryptoHack/general.html#enc-base64)
convert the message from hex to bytes
use the know part of the flag to get the partial key (myXORke)
since we now know the partial, we can try guess the full key. by adding a 'y' we turn ke into key.
repeat the key for the number of times required to decode the message
print the decoded message

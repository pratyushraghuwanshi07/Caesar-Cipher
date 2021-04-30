# Caesar-Cipher
Here is some basic information on how a caesar cipher works.
Both python(.py) and Jupyter Notebook(.ipynb) files are present. Contains files for both encrypting and decrypting. Just download or clone it to use it.

To pass an encrypted message from one person to another, it is first necessary that both parties have the 'key' for the cipher, so that the sender may encrypt it and the receiver may decrypt it. For the caesar cipher, the key is the number of characters to shift the cipher alphabet.

Here is a quick example of the encryption and decryption steps involved with the caesar cipher. The text we will encrypt is 'defend the east wall of the castle', with a shift (key) of 1.

plaintext:  defend the east wall of the castle
ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

It is easy to see how each character in the plaintext is shifted up the alphabet. Decryption is just as easy, by using an offset of -1.

plain:  abcdefghijklmnopqrstuvwxyz
cipher: bcdefghijklmnopqrstuvwxyza

Obviously, if a different key is used, the cipher alphabet will be shifted a different amount.



Mathematical Description

First we translate all of our characters to numbers, 'a'=0, 'b'=1, 'c'=2, ... , 'z'=25. We can now represent the caesar cipher encryption function, e(x), where x is the character we are encrypting, as:
e(x) = (x + k)(mod 26)

Where k is the key (the shift) applied to each letter. After applying this function the result is a number which must then be translated back into a letter.
The decryption function is :
e(x) = (x - k)(mod 26)

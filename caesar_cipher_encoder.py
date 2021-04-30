#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Caesar Cipher Encoder

def encode(plaintext,key):
    encrypted_text = ''
    size = len(plaintext)
    for i in range(0,size):
        single_char = plaintext[i]
        if (single_char.isupper()):
            encrypted_text += chr((ord(single_char) + key-65)% 26+65)
        else:
            encrypted_text += chr((ord(single_char) + key-97)% 26+97)
    return encrypted_text
plaintext = input("Enter Plain Text: ")
key = int(input("Enter key in integer format: "))
print("Encrypted Text : ",encode(plaintext,key))


# In[ ]:





# In[ ]:





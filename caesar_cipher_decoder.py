#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Caesar Cipher Decoder

def decode(encrypted_text,key):
    plaintext = ''
    size = len(encrypted_text)
    for i in range(0,size):
        single_char = encrypted_text[i]
        if (single_char.isupper()):
            plaintext += chr((ord(single_char) + 26-key-65)% 26+65)
        else:
            plaintext += chr((ord(single_char) + 26-key-97)% 26+97)
    return plaintext
encrypted_text = input("Enter Encrypted Text: ")
key = int(input("Enter key in integer format: "))
print("Plain Text : ",decode(encrypted_text,key))


# In[ ]:





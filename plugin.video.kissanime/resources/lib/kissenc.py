#!/usr/bin/env python
"""
Kissasian and Kisscaroon decryption
Created by: Twoure
Date:       06/06/2016
Changed to work with Kodi Addons 06/07/2016 Prometheusx
"""
import binascii
from sha2 import sha256 as SHA256

#import base64
from crypto.cipher.aes_cbc import AES_CBC

class KissDecrypt:
    def __init__(self):
        #kissasian
        #di = base64.b64decode("XzMyYjgxMmU5YTEzMjFhZTBlODRhZjY2MGM0NzIyYjNhXw==")[1:-1]
        #self.derived_drama_iv = binascii.a2b_hex(di)
        #kisscartoon
        #ci = base64.b64decode("X2E1ZThkMmU5YzE3MjFhZTBlODRhZDY2MGM0NzJjMWYzXw==")[1:-1]
        #self.derived_cartoon_iv = binascii.a2b_hex(ci)
        #kissanime
        #ai = base64.b64decode("X2E1ZThkMmU5YzE3MjFhZTBlODRhZDY2MGM0NzJjMWYzXw==")[1:-1]
        ai = 'X2E1ZThkMmU5YzE3MjFhZTBlODRhZDY2MGM0NzJjMWYzXw=='.decode('base-64')[1:-1]
        self.derived_anime_iv = binascii.a2b_hex(ai)

    def ensure_unicode(self, v):
        if isinstance(v, str):
            v = v.decode('utf8')
        return unicode(v)
		
    def decrypt(self, f, kind, rsk):#url=None, headers=None, post_data=None):
        """
        decrypt video URL input depending on what site it came from
        """	
        #if kind == 'anime':
            #rsk = base64.b64decode("X25oYXNhc2RiYXNkdGVuZTcyMzBhc2Jf")[1:-1]            
            #rsk = binascii.a2b_hex('77523155af8cbed35649d6b9ad2f6a9596609be26cde24ee0334b80ae673b803')
            #rsk = '77523155af8cbed35649d6b9ad2f6a9596609be26cde24ee0334b80ae673b803'.decode('hex')
            #rsk = '9msn324s793240cmzxcn'		
        
        derived_key = SHA256(rsk).digest()
        return self.decrypt_input(f, derived_key, self.derived_anime_iv)
		
    def decrypt_input(self, f, key, iv):
        """decrypt video URL"""
        cipher = AES_CBC(key=key, keySize=32)
        return self.ensure_unicode(cipher.decrypt(binascii.a2b_base64(f), iv))	

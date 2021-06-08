from os import getenv
import sqlite3
import win32crypt
import binascii
import base64
import json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def get_string(local_state):
    with open(local_state, 'r', encoding='utf-8') as f:
        s = json.load(f)['os_crypt']['encrypted_key']
    return s


def pull_the_key(base64_encrypted_key):
    encrypted_key_with_header = base64.b64decode(base64_encrypted_key)
    encrypted_key = encrypted_key_with_header[5:]
    key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return key


def decrypt_string(key, data):
    nonce, cipherbytes = data[3:15], data[15:]
    aesgcm = AESGCM(key)
    plainbytes = aesgcm.decrypt(nonce, cipherbytes, None)
    plaintext = plainbytes.decode('utf-8')
    return plaintext


# local_state = getenv("APPDATA") + \
    # r"\..\Local\Microsoft\Edge\User Data\Local State"

local_state = r"E:\Sk_Tools\Google Chrome\User Data\Local State"

# path = getenv("APPDATA") + \
    # r"\..\Local\Microsoft\Edge\User Data\Default\Login Data"
path = r"E:\Sk_Tools\Google Chrome\User Data\Default\Login Data"
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute('SELECT action_url, username_value, password_value FROM logins')

for result in cursor.fetchall():
    print(result)
    if result[2][0:3] == b'v10':
        key = pull_the_key(get_string(local_state))
        password = decrypt_string(key, result[2])
    else:
        try:
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)
        except Exception:
            password = ""
    print(result[0], result[1], password)

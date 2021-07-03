#!/usr/bin/env python3

# Created by Master
# On: 6/27/2021 at 9:42 PM
from binascii import unhexlify

from Cryptodome.Cipher import AES
import hashlib
import base64

from Cryptodome.Util.Padding import unpad

IV: bytes = bytes.fromhex('00060904000609040006090400060904')


def decrypt(data: bytes, secret_key: bytes) -> bytes:
    cipher = AES.new(secret_key, mode=AES.MODE_OFB, iv=IV)
    decrypted = cipher.decrypt(
        unhexlify(data)
    )
    return decrypted


def decrypt_no_time(data: bytes, secret_key: bytes) -> bytes:
    # TODO
    # AES/CBC/PKCS7Padding
    # cipher = AES.new(secret_key, mode=AES.MODE_CBC)
    return None

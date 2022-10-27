""" Encryption for passwords """
import base64, os, sys

from cryptography.fernet import Fernet
key = base64.urlsafe_b64encode(bytes('UniversityOfTheFraserValley2022=', encoding="utf-8"))


def encrypt(key_):
    cipher_suite = Fernet(key_)
    ciphered_text = cipher_suite.encrypt(b"BrianTest123")  # required to be bytes
    print(ciphered_text)
    return ciphered_text


def decrypt(key_, text_in):
    cipher_suite = Fernet(key_)
    ciphered_text = text_in
    unciphered_txt = cipher_suite.decrypt(ciphered_text)
    print(unciphered_txt)


if __name__ == '__main__':

    password = encrypt(key)
    decrypt(key, password)

    sys.exit(os.EX_OK)

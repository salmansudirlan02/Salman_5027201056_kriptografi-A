import string
import requests

url = "http://aes.cryptohack.org/ecb_oracle/{}"

def encrypt(plaintext):
    return requests.get(url.format(plaintext)).json()['ciphertext']
def split(text, size):
    return [text[i:i+size] for i in range(0, len(text),size)]

flag = b''

while b'}' not in flag:
    l = 15 - len(flag) % 16
    for c in string.printable:
        payload = (b'A' * l + flag + c.encode() + b'A' * l).hex()
        blocks = split(encrypt(payload), 32)
        pos = len(flag) // 16
        if len(blocks[pos:]) != len(set(blocks[pos:])):
            flag += c.encode()
            print(flag)
            break
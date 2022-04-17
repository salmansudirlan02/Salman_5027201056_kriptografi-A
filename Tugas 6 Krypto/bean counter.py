import requests
from pwn import xor

image=b'\X89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

ciphertext=bytes.fromhex(requests.get('http://aes.cryptohack.org/bean_counter/encrypt').json()['encrypted'])
key=xor(ciphertext[:16], image)

plaintext = xor(ciphertext, key)
with open('image.jpg', 'wb') as f :
    f.write(plaintext)
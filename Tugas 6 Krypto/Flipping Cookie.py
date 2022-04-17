import requests
from pwn import xor

cookie = requests.get('http://aes.cryptohack.org/flipping_cookie/get_cookie').json()['cookie']
cookie = bytes.fromhex(cookie)

iv = cookie[:16]
cookie = cookie[16:]

iv = xor(iv, b'admin=False;expi', b'admin=True;aaaaa')

print(requests.get('http://aes.cryptohack.org/flipping_cookie/check_admin/{}/{}/'.format(cookie.hex(), iv.hex())).json())
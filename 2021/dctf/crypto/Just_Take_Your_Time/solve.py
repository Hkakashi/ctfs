import time
from Crypto.Cipher import DES3

from pwn import *

r = remote('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', 9999)

r.recvuntil('Show me you are worthy and solve for x! You have one second.\n')

line = r.recvline()

a = int(line.decode().split('*')[0].strip())
b = int(line.decode().split('*')[1].strip()[:-2])

r.sendline(str(a*b))

r.recvuntil('You have proven yourself to be capable of taking on the final task. Decrypt this and the flag shall be yours!\n')

key = str(int(time.time())).zfill(16).encode("utf-8")

secret = r.recvline().decode()

print(secret)

cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
flag = cipher.decrypt(bytes.fromhex(secret))

print(flag)

r.sendline(flag)

r.interactive()
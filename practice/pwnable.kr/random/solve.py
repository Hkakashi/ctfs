from pwn import *

r = ssh("random", "pwnable.kr", 2222, 'guest')

p = r.process('./random')

p.sendline("3039230856")
p.interactive()

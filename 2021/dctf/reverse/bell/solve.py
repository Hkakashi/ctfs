from pwn import *


def triangle(param_1, param_2):
    if (param_1 < param_2):
        lVar1 = 0
    else:
        if ((param_1 == 1) and (param_2 == 1)):
            lVar1 = 1
        else:
            if (param_2 == 1):
                lVar1 = triangle(param_1 + -1, param_1 + -1)
            else:
                lVar2 = triangle(param_1, param_2 + -1)
                lVar1 = triangle(param_1 + -1, param_2 + -1)
                lVar1 = lVar1 + lVar2
    return lVar1


r = remote('dctf-chall-bell.westeurope.azurecontainer.io', 5311)

number = int(r.recvline().strip())

iter = 1

while(iter <= number):
    correct = triangle(number, iter)
    r.sendline(str(correct))
    iter += 1

r.interactive()

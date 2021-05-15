
def func4(i):
    if i < 1:
        i1 = 0
    else:
        if i == 1:
            i1 = 1
        else:
            i2 = func4(i - 1)
            i1 = func4(i - 1)
            i1 = i1 + i2
    return i1

li = [1, 0x7b, 0x3b18, 0x1c640d]
lVar2 = func4(10)
for lVar1 in li:
    print(lVar1 * lVar2)
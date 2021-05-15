import string

def func3_1(char):
    char1 = ''
    if ('@' < char) and (char < '['):
        # if it is capital character
        char = chr(ord(char) + -0xd)
        if char < 'A':
            char1 = b'\x1a'
        else:
            char1 = b'\0'
        char = chr(ord(char1) + ord(char))
    if ('`' < char) and (char < '{'):
        # if it is lower case
        char = chr(ord(char) + -0xd)
        if char < 'a':
            char1 = b'\x1a'
        else:
            char1 = b'\0'
        char = chr(ord(char1) + ord(char))
    return char

def func3_2(char):
    char1 = ''
    if (' ' < char) and (char != '\x7f'): # 32 127
        char = chr(ord(char) + -0x2f) # 47
        if char < '!': # 33
            char1 = '^' # 94
        else:
            char1 = b'\0'
        char = chr(ord(char1) + ord(char))
    return char

dic = {}
for c in string.printable:#"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    try:
        dic[func3_2(func3_1(c))] = c
        # print(i + ' : ' + dic[i])
    except ValueError:
        continue
# print(dic)

encoded = "\"_9~Jb0!=A`G!06qfc8\'_20uf6`2%7"
flag = ""
for c in encoded:
    try:
        flag += dic[c]
    except:
        print(c)
        flag += ' '
print(flag)
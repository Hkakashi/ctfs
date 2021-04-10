import zlib
# 86 7c 21 99 50

with open("enc","rb") as g:
	cipher = g.read()

flag = b"actf{"

key = []
for i in range(5):
    key.append(flag[i] ^ cipher[i])
print(bytes(key[:-1]))

for i in range(256):
    for j in range(256):
        key = bytes([i, j])
        # print(key)
        output = zlib.crc32(key).to_bytes(4,'big')
        # print(output)
        if output == b'\x86|!\x99':
            print(key)
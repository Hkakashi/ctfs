from PIL import Image

src = Image.new('RGB', (600, 500))

file=1
for j in range(1,61):
    for i in range(1,51):
        dst=Image.open('60x50/'+str(file)+'.jpg')
        if(j==1):
            column=1
        else:
            column=(int(j)-1)*10
        if(i==1):
            row=1
        else:
            row=(int(i)-1)*10
        src.paste(dst, (column, row))
        file=int(file)+1
src.save('final.png')

from PIL import Image
import os

l=os.listdir('input')
x=1

for i in l:
    if i.endswith('.webp'):
        name='input/'+i
        img=Image.open(name).convert("RGB")
        y='output/img'+str(x)+'.png'
        img.save(y,"png")
        img.close()
        x=x+1
        print(y)

    else:
        continue

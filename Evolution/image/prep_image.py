from sys import argv
from PIL import Image

image = Image.open(argv[1])
im = image.getdata()
with open('image_data.txt','w') as f:
    f.write(str(image.width)+'\n')
    f.write(str(image.height)+'\n')
    for pix in im:
        f.write(','.join(str(i) for i in pix)+'\n')





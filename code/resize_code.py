# Script for re-sizing/shrinking photos

import PIL
from PIL import Image
import os
os.chdir('/home/benbrew88/Desktop/pics')


for number in range(3)[1:]:
    img = Image.open(str(number) + '.jpg')
    img = img.resize((600, 400), PIL.Image.ANTIALIAS)
    img.save(str(number) + '_big.jpg')





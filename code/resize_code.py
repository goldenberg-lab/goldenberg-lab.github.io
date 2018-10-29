# Script for re-sizing/shrinking photos

import PIL
from PIL import Image
import os
os.chdir('/home/benbrew/Desktop/pics')


for number in range(2)[1:]:
    img = Image.open(str(number) + '.png')
    img = img.resize((600, 400), PIL.Image.ANTIALIAS)
    img.save(str(number) + '_big.png')





# Script for re-sizing/shrinking photos

import PIL
from PIL import Image
import os
os.chdir('/home/ben/Desktop/lab_pics')


for number in range(2)[1:]:
    img = Image.open(str(number) + '.png')
    img = img.resize((180, 205), PIL.Image.ANTIALIAS)
    img.save(str(number) + '_new.png')





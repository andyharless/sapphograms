'''
Main program to create a Sapphogram.
Output a "signle pixels only" picture, and enlarged picture,
and a text file with the hexadecimal values of the pixels.
'''

from fragment import create_sapphogram
from PIL import Image
from current import FRAGMENT, DIMS
from config import PALE
import numpy as np

v = '8'

fragment = str(FRAGMENT)
im = create_sapphogram(f'data/fragment{fragment}greek.txt', shift=PALE)
im.save(f'output/sappho{fragment}v{v}small.png')
im_large = im.resize(DIMS, resample=Image.NEAREST)
im_large.save(f'output/sappho{fragment}v{v}large.png')

with open(f'output/sappho{fragment}img_data_v{v}.txt', 'w') as f:
    print(np.vectorize(hex)(np.array(im)), file=f)

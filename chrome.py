'''
Main program to create a Sapphogram.
Output a "signle pixels only" picture, and enlarged picture,
and a text file with the hexadecimal values of the pixels.
'''

from sys import argv
from fragment import create_sapphogram
from PIL import Image
from current import FRAGMENT, DIMS
import config
import numpy as np

default_shift = 'VIOL'
default_version = '8'

tint = default_shift if len(argv) < 2 else argv[1]
shift = eval(f'config.{tint}')

v = default_version if len(argv) < 3 else argv[2]

fragment = str(FRAGMENT)
im = create_sapphogram(f'data/fragment{fragment}greek.txt', shift=shift)
im.save(f'output/sappho{fragment}v{v}_{tint}_small.png')
im_large = im.resize(DIMS, resample=Image.NEAREST)
im_large.save(f'output/sappho{fragment}v{v}_{tint}_large.png')

with open(f'output/sappho{fragment}img_data_v{v}_{tint}.txt', 'w') as f:
    print(np.vectorize(hex)(np.array(im)), file=f)


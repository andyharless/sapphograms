from fragment import create_sapphogram
from PIL import Image
from current import FRAGMENT, DIMS
import numpy as np

fragment = str(FRAGMENT)
im = create_sapphogram(f'data/fragment{fragment}greek.txt')
im.save(f'output/sappho{fragment}v0small.png')
im_large = im.resize(DIMS, resample=Image.NEAREST)
im_large.save(f'output/sappho{fragment}v0large.png')

with open(f'output/sappho{fragment}img_data.txt', 'w') as f:
    print(np.vectorize(hex)(np.array(im)), file=f)

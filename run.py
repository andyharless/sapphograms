from fragment import create_sapphogram
from PIL import Image
from current import FRAGMENT, DIMS

fragment = str(FRAGMENT)
im = create_sapphogram(f'data/fragment{fragment}greek.txt')
im.save(f'output/sappho{fragment}v0small.png')
im_large = im.resize(DIMS, resample=Image.NEAREST)
im_large.save('output/sappho{fragment}v0large.png')
    

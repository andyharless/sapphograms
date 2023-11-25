from PIL import Image
from fragment import create_sapphogram
from current import FRAGMENT, LONGDIMS, GAP
import math
import numpy as np

fragment = str(FRAGMENT)
fp = f'data/fragment{fragment}greek.txt'
with open(fp) as f:
    poem = f.read()
    
strophes = poem.split('\n\n')

sapphograms = [create_sapphogram(None, strophe, orange=True) 
                for strophe in strophes]

widths, heights = zip(*[im.size for im in sapphograms])
totwidth = math.lcm(*widths)
multipliers = [totwidth//width for width in widths]
newheights = [m*h for h, m in zip(heights, multipliers)]
fullheight = sum(newheights) + GAP*(len(newheights) - 1)

full_image = Image.new('RGB', (totwidth, fullheight))
location = (0, 0)
for s, h in zip(sapphograms, newheights):
    dims = (totwidth, h)
    full_image.paste(s.resize(dims, resample=Image.NEAREST), location)
    location = (0, location[1]+h+GAP)

full_image.save(f'output/sappho{fragment}v6small.png')
im_large = full_image.resize(LONGDIMS, resample=Image.NEAREST)
im_large.save(f'output/sappho{fragment}v6large.png')

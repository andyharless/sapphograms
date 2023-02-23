from fragment import create_sapphogram
from PIL import Image

im = create_sapphogram('data/fragment47.txt')
im.save('output/sappho47v0small.png')
im_large = im.resize((500,300), resample=Image.NEAREST)
im_large.save('output/sappho47v0large.png')
    

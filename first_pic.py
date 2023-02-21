from PIL import Image
import numpy as np
a = np.array([
 [(0x87,0xb7,0x17), (0xB7,0x97,0xD7), (0xB7,0x87,0x8F), (0x87,0xE7,0x1F)],
 [(0x2F,0xB7,0x87), (0x8F,0x87,0xE4), (0x47,0x27,0xCF), (0x97,0x07,0xD7)],
 [(0xB7,0x87,0x8F),  (0x87,0xB7,0x97),  (0x17,0xDF,0x2F),  (0x87,0x8f,0x87)]
             ])
im = Image.fromarray(a.astype(np.uint8), 'RGB')
im.save('../sappho8v0small.png')
im_large = im.resize((400,300), resample=Image.NEAREST)
im_large.save('../sappho8v0large.png')
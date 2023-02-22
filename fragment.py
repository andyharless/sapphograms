import numpy as np
from PIL import Image


ACCENT_REMOVALS = {
                  'Ἄ':'Α', 
                  'έ':'ε',
                  }
                  
def replace_by_dict(s, d):
    '''Do multiple replacements in a string, as specificed by a dictionary
    '''
    out = s
    for k, v in d.items():
        out = out.replace(k, v)
    return out

def deal_with_gaps(s):
    '''
    Translate brackets into gaps, represented by '&'
    and create a parallel list inidcating which letters are hypotehtical
    '''
    len_orig = len(s)
    open_bracket_found = False
    close_bracket_found = False
    hypothetical = [False] * len_orig
    deletions = [False] * len_orig
    outc = list(s)
    for i,c in enumerate(s):
        close_bracket_found |= (c == ']')
        open_bracket_found |= (c == '[')
        # Open bracket indicates a gap
        if c == '[':
            outc[i] = '&'
        if close_bracket_found and not open_bracket_found:
            # Close bracket shows a gap at start of line
            # Mark all prior characters as hypothetical
            # and shift them forward so they appear after gap
            for j in range(i,0,-1):
                outc[j] = outc[j-1]
                hypothetical[j] = True
            # Indicate a gap at the beginning of the line
            outc[0] = '&'
            # Reset gap tracker since next characters will be actual
            close_bracket_found = False
        elif open_bracket_found and not close_bracket_found:
            # We are going through a bracketed part of the line
            if outc[i] not in '&\n':
                hypothetical[i] = True
        elif close_bracket_found:
            # Bracketed part of line (if any) is finished, so reset
            open_bracket_found = False
            close_bracket_found = False
            # Delete current char since open bracket already indicated a gap
            deletions[i] = True
    for i in range(len_orig):
        if deletions[i]:
            del outc[i]
            del hypotheical[i]
    return ''.join(outc), hypothetical

def fix_line(line):
    '''Process line, returning revised line and mask for hypothetical letters
    '''
    # Strip lead/trailing spaces and remove accents (but keep newline at end)
    s = replace_by_dict(line.strip() + '\n', ACCENT_REMOVALS)

    # Eliminate multiple spaces
    doublespace = '  '
    singlespace = ' '
    while doublespace in s:
        s = s.replace(doublespace, singlespace)
        
    # Process gaps
    return deal_with_gaps(s)
                
def read_fragment(fp):
    '''Read a Sappho fragment and convert to Sapphogram sequence
    '''

    CHAR_ARRAY = 'ΣΛΝΜΦΘΧΖΤΔΚΓΨΞΠΒ&\n ";,.\'ΥΙΟΕΡΑΩΗ'

    # Read input line by line
    with open(fp) as f:
        lines = f.readlines()
        
    # Process and concatenate lines and associated flags
    flags = []
    chars = ''
    for line in lines:
        curline, curflags = fix_line(line)
        chars += curline
        flags += curflags
    
    # Remove terminating newline at end of fragment if present
    if chars[-1] == '\n':
        chars = chars[:-1]
        flags.pop()
                
    result = b''    # initialize to empty byte array
    lastchar = '$'  # initialize to nonexistent character

    for c, f in zip(chars, flags):
  
        hypothetical = f      # flag indicates character not in actual fragment
        strange = False       # code for bit 2 (currently unused)

        cap = c.isupper()
        c = c.upper()
        if c in CHAR_ARRAY:
            lastchar = c
            n = CHAR_ARRAY.index(c)
            n <<= 3
            n += (6 if cap else 7)
            n -= (2 if hypothetical else 0)
            n -= (4 if strange else 0)
            if n > 0xFF:
                raise ValueError('bug: n is too big')
            result += bytes([n])
        
    return result
    
def best_aspect(array_length):
    return 4, 3

def create_sapphogram(fp):

    #  Read and convert the data
    data = read_fragment(fp)
    
    #  Pad final pixel if necessary
    if len(data) % 3:
        padding = (len(data) // 3 + 1) - len(data)
        data += bytes([0x97] * padding)
    assert not len(data) % 3
    
    #  Convert pixels to numeric form
    pixels = []
    for i in range(0, len(data), 3):
        pixels.append([int(i) for i in data[i:i+3]])
       
    #  Reshape pixels into a rectangle
    width, height = best_aspect(len(pixels))
    channels = 3
    a = np.array(pixels).reshape(height, width, channels)
    
    # Create a picture
    return Image.fromarray(a.astype(np.uint8), 'RGB')

if __name__=='__main__':
    im = create_sapphogram('data/fragment8_simplified.txt')
    im.save('output/sappho8v1small.png')
    im_large = im.resize((400,300), resample=Image.NEAREST)
    im_large.save('output/sappho8v1large.png')        
    
    print(np.vectorize(hex)(pixels))
    


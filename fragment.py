'''Funcitons comprising the guts of the Sapphogram project'''

import numpy as np
from PIL import Image
from math import sqrt, floor, ceil
from utils import ACCENT_REMOVALS

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
            del hypothetical[i]
    return ''.join(outc), hypothetical

def fix_line(line):
    '''Process line, returning revised line and mask for hypothetical letters
    '''
    # Strip lead/trailing spaces and remove accents (but keep newline at end)
    s = replace_by_dict(line.strip() + '\n', ACCENT_REMOVALS)

    # Eliminate multiple spaces and multiple brackets
    left2 = '[['
    left = '['
    right2 = ']]'
    right = ']'
    space2 = '  '
    space = ' '
    while space2 in s:
        s = s.replace(space2, space)
    while left2 in s:
        s = s.replace(left2, left)
    while right2 in s:
        s = s.replace(right2, right)
        
    # Process gaps
    return deal_with_gaps(s)
                
def read_fragment(fp):
    '''Read a Sappho fragment and convert to Sapphogram sequence
    '''

    CHAR_ARRAY = 'ΣΛΝΜΦΘΧΖΤΔΚΓΨΞΠΒ&\n ";,.\'ΥΙΟΕΡΑΩΗw'

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
            if lastchar == 'Σ' and c == 'w':  # special case digamma in frag 1
                n = int(result[-1]) + 4  # render sigma & clear non-strange bit
                result = result[:-1]     # remove previously added character
            if n > 0xFF:
                raise ValueError('bug: n is too big')
            result += bytes([n])
        
    return result
    
def best_aspect(array_length):
    '''
    Get pixel dimensions for an aspect ratio between 2:1 and 1:1 (inclusive)
    that is a best fit for the total number of pixels to accommodate
    '''
    minwidth = ceil(sqrt(array_length))
    maxwidth = floor(sqrt(2*array_length))

    # First be optimistic and look for a perfect fit
    for w in range(minwidth, maxwidth+1):
        if not array_length % w:
            return(w, array_length // w, 0)

    best = (None, None, None)
    best_npad = 99999
    for w in range(minwidth, maxwidth+1):
        h = ceil(array_length / w)
        npad = h * w - array_length
        if npad < best_npad:
            best = (w, h, npad)
            best_npad = npad
    return best

def create_sapphogram(fp):
    '''Create a visual encoding for a Sappho fragment'''

    #  Read and convert the data
    data = read_fragment(fp)
    
    #  Pad final pixel if necessary
    if len(data) % 3:
        padding = 3 * (len(data) // 3 + 1) - len(data)
        data += bytes([0x97] * padding)
    assert not len(data) % 3
    
    #  Convert pixels to numeric form
    pixels = []
    for i in range(0, len(data), 3):
        pixels.append([int(i) for i in data[i:i+3]])
       
    #  Reshape pixels into a rectangle
    width, height, padding = best_aspect(len(pixels))
    if not width:
        raise ValueError('Cannot find acceptable dimensions')
    start_pad = padding // 2
    end_pad = padding - start_pad
    black = [0,0,0]
    pixels = [black]*start_pad + pixels + [black]*end_pad
    
    channels = 3
    a = np.array(pixels).reshape(height, width, channels)
    
    # Create a picture
    return Image.fromarray(a.astype(np.uint8), 'RGB')


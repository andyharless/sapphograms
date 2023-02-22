def read_fragment(fp):
    '''Read a Sappho fragment and convert to Sapphogram sequence
    '''

    CHAR_ARRAY = 'ΣΛΝΜΦΘΧΖΤΔΚΓΨΞΠΒ&\n ";,.\'ΥΙΟΕΡΑΩΗ'

    with open(fp) as f:
      chars = f.read().replace('[', '&')

    result = b''
    lastchar = '$'  # initialize to nonexistent character

    for c in chars:
  
        # will have to fix these later
        hypothetical = False
        strange = False       # code for bit 2

        cap = c.isupper()
        c = '&' if c==']' else c.upper()
        if c in CHAR_ARRAY and not (c == lastchar == ' '):
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
        
if __name__=='__main__':
    print(bytes(read_fragment('data/fragment8.txt')))

        

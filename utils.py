ACCENT_REMOVALS = {
                  'Ἄ': 'Α', 
                  'Ἔ': 'Ε',
                  '᾿': "'",  # e1bebf in UTF-8 -> regular apostrophe
                  'ἄ': 'α',  # e1bc84 in UTF-8 -> regular alpha
                  'ὰ': 'α',  # e1bdb0 in UTF-8 -> regular alpha
                  'ἀ': 'α',  # e1bc80 in UTF-8 -> regular alpha
                  'ά': 'α',  # ceac in UTF-8 -> regular alpha
                  'ἐ': 'ε',  # e1bc90 in UTF-8 -> regular epsilon
                  'έ': 'ε',  # cead in UTF-8 -> regular epsilon
                  'ί': 'ι',
                  'ό': 'ο',
                  'ύ': 'υ',
                  'ὦ': 'ω',  # e1bda6 in UTF-8 -> regular omega
                  }

def utf(c):
    return hex(int.from_bytes(bytes(c, 'utf-8'), 'big'))
    
def showchars(fp):
    with open(fp) as f:
        s = f.read()
    for i,c in enumerate(s):
        print(i, c, utf(c))

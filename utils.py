ACCENT_REMOVALS = {
                  'Ἀ': 'Α',  # e1bc88 in UTF-8 -> capital alpha
                  'Ἄ': 'Α',  # e1bc8c in UTF-8 -> capital alpha
                  'Ἔ': 'Ε',
                  '᾿': "'",  # e1bebf in UTF-8 -> regular apostrophe
                  '’': "'",  # e28099 in UTF-8 -> regular apostrophe
                  'ἂ': "α",  # e1bc82 in UTF-8 -> regular alpha
                  'ἄ': 'α',  # e1bc84 in UTF-8 -> regular alpha
                  'ὰ': 'α',  # e1bdb0 in UTF-8 -> regular alpha
                  'ἀ': 'α',  # e1bc80 in UTF-8 -> regular alpha
                  'ά': 'α',  #   ceac in UTF-8 -> regular alpha
                  'ἐ': 'ε',  # e1bc90 in UTF-8 -> regular epsilon
                  'ἔ': 'ε',  # e1bc94 in UTF-8 -> regular epsilon
                  'ὲ': 'ε',  # e1bdb2 in UTF-8 -> regular epsilon
                  'έ': 'ε',  #   cead in UTF-8 -> regular epsilon
                  'ὴ': 'η',  # e1bdb4 in UTF-8 -> regular eta
                  'ῃ': 'η',  # e1bf83 in UTF-8 -> regular eta
                  'ἴ': 'ι',  # e1bcb4 in UTF-8 -> regular iota
                  'ὶ': 'ι',  # e1bdb6 in UTF-8 -> regular iota
                  'ί': 'ι',  #   ceaf in UTF-8 -> regular iota
                  'ό': 'ο',
                  'ὄ': 'ο',  # e1bd84 in UTF-8 -> regular omicron
                  'ύ': 'υ',
                  'ὠ': 'ω',  # e1bda0 in UTF-8 -> regular omega
                  'ὦ': 'ω',  # e1bda6 in UTF-8 -> regular omega
                  'ώ': 'ω',  #   cf8e in UTF-8 -> regular omega 
                  'ῳ': 'ωι', # e1bfb3 in UTF-8 -> omega + iota
                  }

def utf(c):
    return hex(int.from_bytes(bytes(c, 'utf-8'), 'big'))
    
def showchars(fp):
    with open(fp) as f:
        s = f.read()
    for i,c in enumerate(s):
        print(i, c, utf(c))

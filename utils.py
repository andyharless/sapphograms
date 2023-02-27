'''Utility functions and data associated with Sapphogram project'''

ACCENT_REMOVALS = {
                  '᾿': "'",  # e1bebf in UTF-8 -> regular apostrophe
                  '’': "'",  # e28099 in UTF-8 -> regular apostrophe
                  '᾽': "'",  # e1bebd in UTF-8 -> regular apostrophe
                  '·': '.',  # c2b7 in UTF-8   -> regular dot
                  'ῤ': 'ρ',  # e1bfa4 in UTF-8 -> regular rho
                  'Ἀ': 'Α',  # e1bc88 in UTF-8 -> capital alpha
                  'Ἄ': 'Α',  # e1bc8c in UTF-8 -> capital alpha
                  'Ἐ': 'Ε',  # e1bc98 in UTF-8 -> capital epsilon
                  'Ἔ': 'Ε',  # e1bc9c in UTF-8 -> capital epsilon
                  'ἀ': 'α',  # e1bc80 in UTF-8 -> regular alpha
                  'ἂ': "α",  # e1bc82 in UTF-8 -> regular alpha
                  'ἄ': 'α',  # e1bc84 in UTF-8 -> regular alpha
                  'ἆ': 'α',  # e1bc86 in UTF-8 -> regular alpha
                  'ὰ': 'α',  # e1bdb0 in UTF-8 -> regular alpha
                  'ά': 'α',  # e1bdb1 in UTF-8 -> regular alpha
                  'ᾶ': 'α',  # e1beb6 in UTF-8 -> regular alpha
                  'ά': 'α',  #   ceac in UTF-8 -> regular alpha
                  'ᾳ': 'αι', # e1beb3 in UTF-8 -> alpha + iota
                  'ἐ': 'ε',  # e1bc90 in UTF-8 -> regular epsilon
                  'ἔ': 'ε',  # e1bc94 in UTF-8 -> regular epsilon
                  'ὲ': 'ε',  # e1bdb2 in UTF-8 -> regular epsilon
                  'έ': 'ε',  # e1bdb3 in UTF-8 -> regular epsilon
                  'έ': 'ε',  #   cead in UTF-8 -> regular epsilon
                  'ἠ': 'η',  # e1bca0 in UTF-8 -> regular eta
                  'ἦ': 'η',  # e1bca6 in UTF-8 -> regular eta
                  'ὴ': 'η',  # e1bdb4 in UTF-8 -> regular eta
                  'ή': 'η',  # e1bdb5 in UTF-8 -> regular eta
                  'ῃ': 'η',  # e1bf83 in UTF-8 -> regular eta
                  'ῆ': 'η',  # e1bf86 in UTF-8 -> regular eta
                  'ή': 'η',  #   ceae in UTF-8 -> regular eta
                  'ἰ': 'ι',  # e1bcb0 in UTF-8 -> regular iota
                  'ἴ': 'ι',  # e1bcb4 in UTF-8 -> regular iota
                  'ὶ': 'ι',  # e1bdb6 in UTF-8 -> regular iota
                  'ί': 'ι',  # e1bdb7 in UTF-8 -> regular iota
                  'ῖ': 'ι',  # e1bf96 in UTF-8 -> regular iota
                  'ί': 'ι',  #   ceaf in UTF-8 -> regular iota
                  'ὀ': 'ο',  # e1bd80 in UTF-8 -> regular omicron
                  'ὄ': 'ο',  # e1bd84 in UTF-8 -> regular omicron
                  'ό': 'ο',  # e1bdb9 in UTF-8 -> regular omicron
                  'ό': 'ο',  #   cf8c in UTF-8 -> regular omicron
                  'ὐ': 'υ',  # e1bd90 in UTF-8 -> regular upsilon
                  'ὔ': 'υ',  # e1bd94 in UTF-8 -> regular upsilon
                  'ὖ': 'υ',  # e1bd96 in UTF-8 -> regular upsilon
                  'ύ': 'υ',  # e1bdbb in UTF-8 -> regular upsilon
                  'ῦ': 'υ',  # e1bfa6 in UTF-8 -> regular upsilon
                  'ύ': 'υ',  #   cf8d in UTF-8 -> regular upsilon
                  'ὠ': 'ω',  # e1bda0 in UTF-8 -> regular omega
                  'ὤ': 'ω',  # e1bda4 in UTF-8 -> regular omega
                  'ὦ': 'ω',  # e1bda6 in UTF-8 -> regular omega
                  'ὼ': 'ω',  # e1bdbc in UTF-8 -> regular omega
                  'ώ': 'ω',  # e1bdbd in UTF-8 -> regular omega
                  'ῶ': 'ω',  # e1bfb6 in UTF-8 -> regular omega
                  'ώ': 'ω',  #   cf8e in UTF-8 -> regular omega 
                  'ῳ': 'ωι', # e1bfb3 in UTF-8 -> omega + iota
                  'ῷ': 'ωι', # e1bfb7 in UTF-8 -> omega + iota
                  }

def utf(c):
    '''Give the UTF heaxdecimal equivlaent of a quoted character'''
    return hex(int.from_bytes(bytes(c, 'utf-8'), 'big'))
    
def showchars(fp):
    '''
    Display the characters from a file one-by-one on separate lines 
    along with their sequence numbers and hexadecimal UTF codes.
    '''
    with open(fp) as f:
        s = f.read()
    for i,c in enumerate(s):
        print(i, c, utf(c))
        
def newchars(fp):
    charlist = 'ΣΛΝΜΦΘΧΖΤΔΚΓΨΞΠΒ&\n ";,.\'ΥΙΟΕΡΑΩΗ' + ']['
    current_set = charlist + charlist.lower()
    current_set += ''.join(ACCENT_REMOVALS.keys()) + 'ς-'
    with open(fp) as f:
        s = f.read()
    for i,c in enumerate(s):
        if c not in current_set:
            print(i, c, utf(c))
    

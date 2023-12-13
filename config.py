# Chrome shift values:
# Elements of each 3-tuple refer to R, G, B channels respectively
# First element of each pair refers to number of bits right shift
# Second element of each pair refers to what to replace those bits with

TANG = ((2, 0b11), (2, 0b01), (3, 0b000))   # Orange
VIOL = ((2, 0b10), (2, 0b01), (2, 0b11))    # Violet
BLUI = ((3, 0b001), (3, 0b011), (2, 0b11)) # Bluish
CYAN = ((1, 0b0), (2, 0b11), (2, 0b11)) # Cyan
PALE = ((2, 0b11), (2, 0b11), (2, 0b11)) # Pale
PALR = ((3, 0b111), (3, 0b111), (3, 0b111)) # Paler
SKYE = ((2, 0b11), (3, 0b111), (3, 0b111)) # Pale cyan
SKYR = ((2, 0b11), (3, 0b111), (4, 0b1111)) # Pale sky blue
SKYT = ((1, 0b1), (3, 0b111), (4, 0b1111)) # Pale bluer cyan
DKBL = ((3, 0b001), (3, 0b001), (2, 0b01)) # Dark blue
DPBL = ((3, 0b001), (3, 0b001), (3, 0b011)) # Deep blue
CHRT = ((1, 0b1), (1, 0b1), (2, 0b00)) # Chartreuse0
YELO = ((2, 0b11), (2, 0b11), (3, 0b000)) # Yellow
GOLD = ((2, 0b11), (1, 0b1), (3, 0b000)) # Gold
REDD = ((2, 0b11), (2, 0b00), (2, 0b00)) # Red
PINK = ((2, 0b11), (1, 0b0), (1, 0b0)) # Pink
BRWN = ((2, 0b01), (2, 0b00), (3, 0b00)) # Brown
BLUE = ((2, 0b00), (2, 0b00), (2, 0b11)) # Blue
GREN = ((2, 0b00), (1, 0b1), (2, 0b00)) # Green
BRGR = ((1, 0b0), (3, 0b111), (1, 0b0)) # Bright green
DUGR = ((2, 0b01), (1, 0b1), (2, 0b01)) # Dull green
PAGR = ((3, 0b011), (2, 0b11), (1, 0b1)) # Pale green
MIGR = ((1, 0b1), (2, 0b11), (1, 0b1)) # Mixed green
DARK = ((1, 0b0), (2, 0b0), (1, 0b0)) # Dark
VDRK = ((2, 0b00), (2, 0b00), (2, 0b00)) # Very dark
UDRK = ((3, 0b000), (3, 0b000), (3, 0b000)) # Ultra dark
BRIT = ((2, 0b11), (2, 0b11), (2, 0b11)) # Bright
PURP = ((2, 0b10), (1, 0b0), (2, 0b11)) # Purple
MAGE = ((2, 0b11), (1, 0b0), (2, 0b11)) # Magenta
BLUV = ((2, 0b10), (1, 0b0), (3, 0b111)) # Blue violet
BBLV = ((3, 0b101), (2, 0b01), (4, 0b1111)) # Bright blue violet
PBLV = ((4, 0b1010), (3, 0b000), (3, 0b111)) # Pure blue violet
BLRV = ((3, 0b011), (3, 0b000), (3, 0b111)) # Bluer violet
BYLO = ((3, 0b111), (3, 0b111), (3, 0b000)) # Bold Yellow
PYLO = ((4, 0b1111), (3, 0b111), (4, 0b0000)) # Plain Yellow

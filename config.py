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
SKYR = ((2, 0b11), (3, 0b111), (4, 0b1111)) # Pale blue cyan
SKYT = ((1, 0b1), (3, 0b111), (4, 0b1111)) # Pale bluer cyan

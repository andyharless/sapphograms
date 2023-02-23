# Sapphograms
Visual Encodings of Sappho Lyrics/Fragments


([Link to original README, which describes the creation of Sapphogram 0](original_readme.md))


The idea is discussed in [this Twitter thread](https://twitter.com/AndyHarless/status/1627705276336857088).




### Procedure for generating a Sapphogram
#### (using the standard Greek alphabest ΑΒΓΔΕΙΖΗΘΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ):
- Start with the Greek text of a Sappho lyric or fragment (e.g., from [The Digital Sappho](https://digitalsappho.org/)).
- Each character or conrol code (e.g. "gap" code meaning there is a gap in the fragment) is represented by one channel (i.e., one byte) of an RGB pixel, so each pixel represents three consecutive letters/codes.
- higher-order bits interpreted as follows:
  - bit 7 clear -> consonants (except rho):  ΒΓΔΖΘΚΛΜΝΞΠΣΤΦΧΨ
    - bit 6 set   -> stops (approximately in modern English pronunciation): ΒΓΔΚΞΠΤΨ (ΒΠ + ΞΨ, ΓΚ + ΔΤ)
    - bit 6 clear -> fricatives (approximately in modern English pronunciation): ΖΘΛΜΝΣΦΧ (ΖΧ + ΘΦ, ΜΝ + ΛΣ)
  - bit 7 set   -> vowels, rho, punctuation, and control codes
    - bit 6 set   -> vowels and rho:  ΑΕΙΗΟΡΥΩ (ΗΩ + ΑΡ, ΕΟ + ΙΥ)
    - bit 6 clear -> punctuation and control codes: (apostrophe,dot + comma,semicolon) + (quote,space + newline,gap)
- lower-order bits interpreted as follows:
  - bits 3, 4, and 5 select within these sets according to the groupings indicated above
    - In each case, a set bit selects the first element of a grouping and a clear bit selects the second.  Thus, for example, Upsilon, being the second member of the second minor grouping of the second major grouping within the "vowels and rho" category, would have all 3 of these bits clear (but 6 and 7 set, so it starts with 11000).
  - bit 2 -> normally set; clear may indicate various things such as characters that are rendered as digamma in some transcriptions
  - bit 1 -> normally set; clear indicates hypothesized text not present in actual fragment
  - bit 0 -> normally set; clear indicates a letter usually capitalized in modern renderings
- Ignore accent and voicing marks (the latter always smooth in Sappho anyhow AFAIK).
- Since the length of the lyric/fragment may not be a multiple of 3, the final pixel is padded with spaces if necessary.
- Aspect ratio of the final Sapphogram is between 2:1 and 1:1 (inclusive).
- Pixels are arranged left-to-right top-to-bottom in a rectangle, with black pixels padding the upper left and lower right as necessary to accommodate texts that don't fit in a rectangle (which will likely be the usual case, I think).
- Black padding pixels to be distributed as evenly as possible between upper left and lower right, with preference to the lower right.
- Subject to the aspect ratio constraint, minimize the number of black padding pixels necessary to accommodate a text.
- Magnify the results as appropriate using squares of identical pixels to represent single pixels from the raw result.

The procedure is implemented in `fragments.py`


### For example:

Sappho's Fragment 8 is reprsented thus at [The Digital Sappho](https://digitalsappho.org/fragments/fr8/):
```
].ν. ο̣ .[
   ] α̣μφ.[
Ἄ]τθι σο.[
   ]. νέφ[
       ]     [
```
(The whitespace has been slightly modified from the version at Digital Sappho, and, as regards whitespace and such, my interpreation here is slightly different than what you will get from reading the characters digitally in sequence.)  Reading this line by line, I get:
```
gap, dot, nu, dot, space, omicron, dot, gap, newline
gap, alpha, mu, phi, dot, gap, newline
gap, alpha (capitalized and hypothetical), tau, theta, iota, space, sigma, omicron, dot, gap, newline
gap, dot, space, nu, epsilon, phi, gap, newline
gap
```
So, according to the representations described above, we have:
```
control characters and punctuation:
gap     = 1000 0111 = 0x87
newline = 1000 1111 = 0x8F
dot     = 1011 0111 = 0xB7
space   = 1001 0111 = 0x97
```
```
vowels:
omicron = 1101 0111 = 0xD7
epsilon = 1101 1111 = 0xDF
alpha   = 1110 1111 = 0xEF
alpha*  = 1110 1100 = 0xEC (capitalized and hypothetical)
```
```
consonants:
mu      = 0001 1111 = 0x1F
nu      = 0001 0111 = 0x17
sigma   = 0000 0111 = 0x07
phi     = 0010 0111 = 0x27
theta   = 0010 1111 = 0x2F
tau     = 0100 0111 = 0x47
```
so the first line `gap, dot, nu, dot, space, omicron, dot, gap, newline` translates into hexadecimal as `87 B7 17 B7 97 D7 B7 87 8F` and into RGB pixels as `87B717 B797D7 B7878F`,
and the full passage transaltes into pixels as follows:
```
87B717 B797D7 B7878F 87EF1F 27B787 8F87EC 472FCF 9707D7 B7878F 87B797 17DF27 878F87
```
Conveniently, no padding is necessary, and it can be arranged in a 4x3 rectangle:
```
87B717 B797D7 B7878F 87EF1F 
27B787 8F87EC 472FCF 9707D7 
B7878F 87B797 17DF27 878F87
```
which I easily rendered using the Python command line with a few run-of-the-mill libraries:
``` 
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from PIL import Image
>>> import numpy as np
>>> a = np.array([[(0x87,0xb7,0x17), (0xB7,0x97,0xD7), (0xB7,0x87,0x8F), (0x87,0xE7,0x1F)],
... [(0x2F,0xB7,0x87), (0x8F,0x87,0xE4), (0x47,0x27,0xCF), (0x97,0x07,0xD7)],
... [(0xB7,0x87,0x8F),  (0x87,0xB7,0x97),  (0x17,0xDF,0x2F),  (0x87,0x8f,0x87)]]
... )
>>> im = Image.fromarray(a.astype(np.uint8), 'RGB')
>>> im.save('sappho8v1small.png')
>>> im_large = im.resize((400,300), resample=Image.NEAREST)
>>> im_large.save('sappho8v1large.png')
```
![sappho8v1large](https://user-images.githubusercontent.com/25837203/220943400-fec4abbb-0390-43eb-b745-bb7e133d786f.png)


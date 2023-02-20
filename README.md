# Sapphograms
Visual Encodings of Sappho Lyrics/Fragments

The idea is discussed in [this Twitter thread](https://twitter.com/AndyHarless/status/1627705276336857088).  *On va voir ce qui se passera*.




Here's what I'm thinking (using the standard Greek alphabest ΑΒΓΔΕΙΖΗΘΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ):
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


### For example:

Sappho's Fragment 8 is reprsented thus at [The Digital Sappho](https://digitalsappho.org/fragments/fr8/):
```
].ν. ο̣ .[
   ] α̣μφ.[
Ἄ]τθι σο.[
   ]. νέφ[
       ]     [
```
Reading this line by line, I get (ignoring a space in the first line that wasn't evident in the browser rendering of the site):
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
alpha   = 1110 0111 = 0xE7
alpha*  = 1110 0100 = 0xE4 (capitalized and hypothetical)
```
```
consonants:
mu      = 0001 1111 = 0x1F
nu      = 0001 0111 = 0x17
sigma   = 0000 0111 = 0x07
phi     = 0010 1111 = 0x2F
theta   = 0010 0111 = 0x27
tau     = 0100 0111 = 0x47
```
so the first line `gap, dot, nu, dot, space, omicron, dot, gap, newline` translates into hexadecimal as `87 B7 17 B7 97 D7 B7 87 8F` and into RGB pixels as `87B717 B797D7 B7878F`,
and the full passage transaltes into pixels as follows:
```
87B717 B797D7 B7878F 87E71F 2FB787 8F87E4 4727CF 9707D7 B7878F 87B797 17DF2F 878f87
```
Conveniently, no padding is necessary, and it can be arranged in a 4x3 rectangle:
```
87B717 B797D7 B7878F 87E71F 
2FB787 8F87E4 4727CF 9707D7 
B7878F 87B797 17DF2F 878f87
```

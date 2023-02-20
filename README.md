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
  - bit 2 -> normally set; clear may indicate various things such as characters that are rendered as digamma in some transcriptions
  - bit 1 -> normally set; clear indicates hypothesized text not present in actual fragment
  - bit 0 -> normally set; clear indicates a letter usually capitalized in modern renderings
- Since the length of the lyric/fragment may not be a multiple of 3, the final pixel is padded with spaces if necessary.
- Aspect ratio of the final Sapphogram is between 2:1 and 1:1 (inclusive).
- Pixels are arranged left-to-right top-to-bottom in a rectangle, with black pixels padding the upper left and lower right as necessary to accommodate texts that don't fit in a rectangle (which will likely be the usual case, I think).
- Black padding pixels to be distributed as evenly as possible between upper left and lower right, with preference to the lower right.
- Subject to the aspect ratio constraint, minimize the number of black padding pixels necessary to accommodate a text.

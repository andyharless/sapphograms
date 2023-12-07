from PIL import Image, ImageDraw, ImageFont
img = Image.open("output/sappho1v9_SKYR_large.png")
draw = ImageDraw.Draw(img)

txt = "Immortal Aphrodite on the thousand-colored throne,\n"
txt += "daughter of Zeus, wile-weaving, I pray you:\n"
txt += "do not overcome my spirit with vexation and sorrow,\n"
txt += "Great Lady,\n\n"

txt += "but come hither if ever and at any other time,\n" 
txt += "hearing my voice from afar,\n"
txt += "you gave heed and, leaving your father's\n"
txt += "golden house, came,\n\n"

txt += "and yoked to your chariot, the beautiful, swift\n"
txt += "sparrows carried you above the black earth\n"
txt += "with their fast-beating wings through the middle\n"
txt += "of the heavenly air:\n\n"

txt += "and suddenly you arrived, blessed one, and\n"
txt += "with your smiling immortal face,\n"
txt += "asked what this time I have suffered and\n"
txt += "why this time I call\n\n"

txt += "and what I most wish for myself in\n"
txt += "my frenzied heart. —And whom this time am I to persuade\n"
txt += "to lead you back into her affection?  Who,\n"
txt += "Sappho, does you injustice?\n\n"

txt += "For even if she flees, she will very soon pursue.\n"
txt += "And if she accepts no gifts, yet she will very soon give.\n"
txt += "And if she does not love, she will very soon love,\n"
txt += "even against her own will.\n\n"

txt += "Come to me even now, and free me from\n"
txt += "painful care, and what most to be accomplished\n"
txt += "my heart desires, accomplish, and you yourself\n"
txt += "be an ally"



font_size = 17
font_path = "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"
font = ImageFont.truetype(font_path, font_size)
draw.text((80, 37), txt, fill =(0, 0, 0), font=font)
img.save('output/fr1skyr_ov.png')
img.show()

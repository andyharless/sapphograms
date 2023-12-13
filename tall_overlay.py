from PIL import Image, ImageDraw, ImageFont
img = Image.open("output/sappho1v8sized.png")
draw = ImageDraw.Draw(img)
txt = "Immortal Aphrodite on the\n"
txt += "      thousand-colored throne,\n\n"
txt += "daughter of Zeus,\n"
txt += "       wile-weaving, I pray you:\n\n"
txt += "do not overcome my spirit\n"
txt += "      with vexation and sorrow,\n\n"
txt += "Great Lady,\n\n\n"

txt += "but come hither if ever\n"
txt += "    and at any other time,\n\n" 
txt += "hearing my voice from afar,\n\n"
txt += "you gave heed and, leaving your\n\n"
txt += "father's golden house, came,\n\n\n"

txt += "            and yoked to your\n" 
txt += "     chariot, the beautiful, swift\n\n"
txt += "sparrows carried\n"
txt += "     you above the black earth\n\n"
txt += "with their fast-beating\n"
txt += "     wings through the middle\n\n"
txt += "of the heavenly air:\n\n\n"

txt += "and suddenly you\n"
txt += "   arrived, blessed one, and\n\n"
txt += "with your smiling immortal face,\n\n"
txt += "asked what this time I\n"
txt += "     have suffered and\n\n"
txt += "why this time I call\n\n\n\n"

txt += "and what I most\n"
txt += "     wish for myself in\n\n\n"
txt += "my frenzied heart. —And whom\n" 
txt += "     this time am I to persuade\n\n\n"
txt += "to lead you back\n"
txt += "     into her affection?  Who,\n\n"
txt += "Sappho, does you injustice?\n\n\n\n"

txt += "For even if she flees,\n"
txt += "     she will very soon pursue.\n\n"
txt += "And if she accepts no gifts, yet she\n"
txt += "     will very soon give them.\n\n"
txt += "And if she does not love,\n"
txt += "     she will very soon love,\n\n"
txt += "even against her own will.\n\n\n\n"

txt += "Come to me even now,\n"
txt += "    and free me from\n\n"
txt += "painful care, and what\n"
txt += "     most to be accomplished\n\n\n"
txt += "my heart desires,\n"
txt += "     accomplish, and you yourself\n\n\n"
txt += "be an ally"

font_size = 16
font_path = "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"
font = ImageFont.truetype(font_path, font_size)
draw.text((16, 5), txt, fill =(0, 0, 0), font=font)
img.save('output/sappho1v8sized_overlay0.png')
img.show()

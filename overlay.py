from PIL import Image, ImageDraw, ImageFont
img = Image.open("output/sappho23v8large.png")
draw = ImageDraw.Draw(img)
txt = "of love\n\n"
txt += "when I look upon you face to face\n\n"
txt += "not even Hermione seems to be like you\n\n"
txt += "but to compare you to fair-haired Helen is not unseemly\n\n"
txt += "mortal women\n\n"
txt += "be assured that\n\n"
txt += "would free me from all my troubles\n\n"
txt += "dewy banks\n\n"
txt += "to stay awake all night"
font_size = 20
font_path = "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"
font = ImageFont.truetype(font_path, font_size)
draw.text((18, 4), txt, fill =(0, 0, 0), font=font)
img.save('output/sappho23english8verlay0.png')
img.show()

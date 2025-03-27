from PIL import Image, ImageDraw, ImageFont

img = Image.open('images/uchiha-1.jpg')

I1 = ImageDraw.Draw(img)

myFont = ImageFont.truetype('fonts/RockSalt-Regular.ttf', 65)

I1.text((10, 10), "Welcome Uchiha Clan", font=myFont, fill="blue")

img.show()

img.save("uchiha-2.png")
from PIL import Image

img = Image.open("images/uchiha-1.jpg")

black_n_white = img.convert("L")

black_n_white.show()

black_n_white.save("images/black_n_white.jpg")

# write some text at the center of the image using pillow

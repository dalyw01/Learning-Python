from PIL import Image

img1 = Image.open("smile.jpg")
img2 = Image.open("sad.jpg")

area = ( 100, 100 )

img1.paste( img2 , area )

img1.show()
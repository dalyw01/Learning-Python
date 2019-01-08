from PIL import Image

# IMPORTANT, the 2 images need to be the same size!

img1 = Image.open("smile.jpg")
img2 = Image.open("smile_2.jpg")

r1,g1,b1 = img1.split()
r2,g2,b2 = img2.split()

new_image = Image.merge( "RGB" , (r2 , g1 , b2) )
new_image.show()

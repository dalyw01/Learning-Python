from PIL import Image

test_image = "smile.jpg"
original = Image.open(test_image)

# - - - - - - - - - - - - - - -
# Display original image first
# - - - - - - - - - - - - - - -

original.show()

# - - - - - - - - -
# 1 Way of doing it
# - - - - - - - - -

width, height = original.size   # Get dimensions

left   = width/4
top    = height/4
right  = 3 * width/4
bottom = 3 * height/4
cropped_example = original.crop((left, top, right, bottom))

cropped_example.show()

# - - - - - - - - - - - - -
# Another way of doing it
# - - - - - - - - - - - - - 

area = ( 100, 100 , 150 , 200 )
cropped_image = original.crop( area )
cropped_image.show()
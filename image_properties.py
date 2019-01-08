from PIL import Image

# pip install Pillow
# Also the I in the "import" above needs to be capilitized!
# https://stackoverflow.com/questions/26505958/why-cant-python-import-image-from-pil

img = Image.open("smile.jpg")
print(img.size)
print(img.format)

img.show()
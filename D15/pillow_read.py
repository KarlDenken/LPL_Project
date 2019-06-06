from PIL import Image, ImageFilter

image = Image.open('test.jpg')
print(image.format, image.size, image.mode)
# image.show()

# Get cropped image
rect = (80, 20, 310, 360)
image.crop(rect).show()

# Get thumbnail image
size = (128, 128)
image.thumbnail(size)
image.show()

# putpixel
for x in range(20, 1500):
  for y in range(30, 40):
    image.putpixel((x, y), (128, 128, 128))

image.show()

# Filter
image.filter(ImageFilter.CONTOUR).show()

from PIL import Image, ImageOps

# Load the original image
image = Image.open('E:/Project/Charity Project Resources/191. front_end_html/uploads/cause_photo_1704072157.jpg')

# Define the padding size (left, top, right, bottom)
padding = (50, 50, 50, 50)  # Add 50 pixels of padding to all sides

# Create a new image with padding around the original image
padded_image = ImageOps.expand(image, border=padding, fill=(255, 0, 0))  # fill is black

# Display the image with padding
padded_image.show()

from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Load the image
image = Image.open('E:/Project/Charity Project Resources/191. front_end_html/uploads/cause_photo_1704072157.jpg')

# Convert image to RGB mode if it is not (ImageOps.invert requires RGB or L mode)
if image.mode != 'RGB':
    image = image.convert('RGB')

# Invert the image (create negative)
negative_image = ImageOps.invert(image)

fig, ax=plt.subplots(1,2)

ax[0].imshow(image)
ax[0].axis('off')
ax[0].set_title('Original Image')

ax[1].imshow(negative_image)
ax[1].axis('off')
ax[1].set_title('Negative Image')
plt.show()
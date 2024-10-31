from PIL import Image
import 

# Load the image
image = Image.open('E:/Project/Charity Project Resources/191. front_end_html/uploads/cause_photo_1704072157.jpg')

# Convert the image to grayscale
gray_image = image.convert('L')

# Define the threshold value (128 is common, but you can adjust it)
threshold = 128

# Apply the threshold to convert the grayscale image to binary
binary_image = gray_image.point(lambda x: 255 if x > threshold else 0, mode='1')

# Display the binary image
fig, ax=plt.subplots(1,2)

ax[0].imshow(image)
ax[0].axis('off')
ax[0].set_title('Original Image')

ax[1].imshow(negative_image)
ax[1].axis('off')
ax[1].set_title('Negative Image')
plt.show()
binary_image.show()

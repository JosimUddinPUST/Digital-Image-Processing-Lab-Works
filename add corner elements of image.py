from PIL import Image
import numpy as np

# Load the image
# image = Image.open('E:\Project\Charity Project Resources\191. front_end_html\uploads\cause_photo_1704072157.jpg')
image = Image.open('E:/Project/Charity Project Resources/191. front_end_html/uploads/cause_photo_1704072157.jpg')

# Convert the image to grayscale
gray_image = image.convert('L')

# Convert the grayscale image to a numpy array
image_array = np.array(gray_image)

# Get the shape of the array (height and width of the image)
height, width = image_array.shape

# Get the corner elements
top_left = image_array[0, 0]
top_right = image_array[0, width - 1]
bottom_left = image_array[height - 1, 0]
bottom_right = image_array[height - 1, width - 1]

top_row= image_array[0,:]
bottom_row=image_array[height-1,:]
left_column=image_array[:,0]
right_column=image_array[:,width-1]

# Add the corner elements
corner_sum = top_left + top_right + bottom_left + bottom_right
# Add the Boundary elements
boundary_sum = (np.sum(top_row) + np.sum(bottom_row) + np.sum(left_column[1:-1]) + np.sum(right_column[1:-1]))



print("Corner elements are:", top_left, top_right, bottom_left, bottom_right)
print("Sum of corner elements:", corner_sum)
print("Sum of boundary elements:", boundary_sum)

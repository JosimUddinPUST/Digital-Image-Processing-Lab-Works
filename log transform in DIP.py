import cv2
import numpy as np

# Load an image
image = cv2.imread('D:\OneDrive\Desktop\DIP Image.png', 0)  # Load as grayscale

# Apply log transformation
c = 255 / np.log(1 + np.max(image))  # Calculate scaling constant
log_image = c * (np.log(1 + image))

# Convert to uint8 for display
log_image = np.array(log_image, dtype=np.uint8)

# Show the images
cv2.imshow('Original Image', image)
cv2.imshow('Log Transformed Image', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load an image
image = cv2.imread('D:\OneDrive\Desktop\DIP Image.png',0)  # Load as grayscale

# Define the gamma value
gamma = 0.5  # Change gamma to experiment with different transformations

# Apply power-law (gamma) transformation
c = 255 / (np.max(image) ** gamma)  # Calculate scaling constant
power_image = c * (image ** gamma)   # Apply the transformation

# Convert to uint8 for display
power_image = np.array(power_image, dtype=np.uint8)

# Show the images
cv2.imshow('Original Image', image)
cv2.imshow(f'Power-Law Transformed Image (Gamma = {gamma})', power_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

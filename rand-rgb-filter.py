import cv2
import numpy as np

# Load the input image
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'
image = cv2.imread(input_image_path)

# Calculate the cumulative sum of the original RGB values
cumulative_sum = np.cumsum(image, axis=0)
cumulative_sum = np.cumsum(cumulative_sum, axis=1)

# Get the shape of the image
height, width, channels = image.shape

# Generate random RGB values while maintaining the same cumulative sum
new_image = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
for c in range(channels):
    for i in range(height):
        for j in range(width):
            if j > 0:
                new_image[i, j, c] += cumulative_sum[i, j - 1, c]
            if i > 0:
                new_image[i, j, c] += cumulative_sum[i - 1, j, c]
            if i > 0 and j > 0:
                new_image[i, j, c] -= cumulative_sum[i - 1, j - 1, c]

# Save the modified image
cv2.imwrite(output_image_path, new_image)

print("Modified image saved as", output_image_path)

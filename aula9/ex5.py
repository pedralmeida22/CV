# import
import numpy as np
import cv2

# Read the image
image = cv2.imread("Orchid.bmp", cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be opened")
    exit(-1)

# Image characteristics
height, width, something = image.shape

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Create a visualization window
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)

# Show the image
cv2.imshow("Display window", image)

# Wait
cv2.waitKey(0)

# Destroy the window -- might be omitted
cv2.destroyWindow("Display window")


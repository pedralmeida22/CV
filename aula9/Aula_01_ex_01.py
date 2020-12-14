# Aula_01_ex_01.py
#
# Example: loading and displaying an image with OpenCV
#
# Paulo Dias - 10/2019


# import
import numpy as np
import cv2

# Read the image
image = cv2.imread("lena.jpg", cv2.IMREAD_UNCHANGED)
# image = cv2.imread("Orchid.bmp", cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be opened")
    exit(-1)

# Image characteristics
print("Image shape - {}".format(image.shape))
height, width = image.shape
# height, width, something = image.shape

print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %s" % image.dtype)

imcopy = image.copy()
print("Image copy shape - {}".format(imcopy.shape))
height, width = imcopy.shape

# for i in range(0, height):
#     for j in range(0, width):
#         if imcopy[i, j] < 128:
#             imcopy[i, j] = 0

for i in range(0, height):
    for j in range(0, width):
        if imcopy.item(i, j) < 128:
            imcopy.itemset(i, j, 0)

# Create a visualization window
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Display copy window", cv2.WINDOW_AUTOSIZE)

# Show the image
cv2.imshow("Display window", image)
cv2.imshow("Display copy window", imcopy)

# Wait
cv2.waitKey(0)

# Destroy the window -- might be omitted
cv2.destroyWindow("Display window")
cv2.destroyWindow("Display copy window")

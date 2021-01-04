# import
import numpy as np
import cv2

img = "lena.jpg"

# Read the image
image = cv2.imread(img, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be opened")
    exit(-1)

ret, bin = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
cv2.imshow("bin", bin)

ret, bin_inv = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("bin_inv", bin_inv)

ret, trunc = cv2.threshold(image, 128, 255, cv2.THRESH_TRUNC)
cv2.imshow("trunc", trunc)

ret, tozero = cv2.threshold(image, 128, 255, cv2.THRESH_TOZERO)
cv2.imshow("tozero", tozero)

ret, tozero_inv = cv2.threshold(image, 128, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("tozero_inv", tozero_inv)

# Create a visualization window
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)

# Show the image
cv2.imshow("Display window", image)

# Wait
cv2.waitKey(0)

# Destroy the window -- might be omitted
cv2.destroyAllWindows()

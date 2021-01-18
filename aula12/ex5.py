import cv2
import numpy as np


##########################
# Print Image Features

def printImageFeatures(image):
    if len(image.shape) == 2:
        height, width = image.shape
        nchannels = 1
    else:
        height, width, nchannels = image.shape

    print("Image Height:", height)
    print("Image Width:", width)
    print("Number of channels:", nchannels)
    print("Number of elements:", image.size)


###################################
# MAIN

# image = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
img = "mon1.bmp"
image = cv2.imread(img, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be open!")
    exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

# ret,thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
# cv2.imshow('threshold', thresh1)

ret,thresh2 = cv2.threshold(image, 90, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('threshold_inv', thresh2)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
img_erode = cv2.erode(thresh2, kernel, iterations=2)
cv2.imshow('erode', img_erode)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
img_erode = cv2.erode(thresh2, kernel, iterations=2)
cv2.imshow('erode9', img_erode)

cv2.waitKey(0)

cv2.destroyAllWindows()

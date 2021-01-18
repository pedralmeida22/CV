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
img = "art2.bmp"
image = cv2.imread(img, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be open!")
    exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

# vertical
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 9))
img_erode = cv2.erode(image, kernel, iterations=1)
# cv2.imshow('Dilation_square', img_erode)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 9))
img_dilation = cv2.dilate(img_erode, kernel, iterations=1)
cv2.imshow('vertical', img_dilation)

# same thing
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 9))
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('vertical2', opening)
#--------------------------------------------------------

# horizontal
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
img_erode = cv2.erode(image, kernel, iterations=1)
# cv2.imshow('Dilation_square', img_erode)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
img_dilation = cv2.dilate(img_erode, kernel, iterations=1)
cv2.imshow('horizontal', img_dilation)

# same thing
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('horizontal2', opening)

cv2.waitKey(0)

cv2.destroyAllWindows()

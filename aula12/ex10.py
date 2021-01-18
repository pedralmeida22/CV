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
img = "fce5noi1.bmp"
img2 = "fce5noi2.bmp"
img3 = "fce5noi3.bmp"
image = cv2.imread(img3, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be open!")
    exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('opening', opening)
# resolve pimenta, sal fica igual

cv2.waitKey(0)

cv2.destroyAllWindows()

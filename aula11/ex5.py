# Aula_03_ex_04.py
#
# Sobel Operator
#
# Paulo Dias - 10/2019


import cv2
import numpy as np
import sys
import math


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
img = "Lena_Ruido.png"
img2 = "DETI_Ruido.png"
img = "lena-saltandpepper.tif"
# img = "fce5noi3.bmp"
# img = "fce5noi4.bmp"
# img = "fce5noi6.bmp"
img = "Bikesgray.jpg"
img = "wdg2.bmp"
image = cv2.imread(img, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be open!")
    exit(-1)

printImageFeatures(image)

cv2.imshow('Original', image)

# canny = cv2.Canny(image, 100, 75)
canny = cv2.Canny(image, 64, 32)

cv2.namedWindow("canny", cv2.WINDOW_AUTOSIZE)
cv2.imshow("canny", canny)

cv2.waitKey(0)

cv2.destroyAllWindows()

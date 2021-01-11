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
img = "tools_2.png"
image = cv2.imread(img, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be open!")
    exit(-1)

printImageFeatures(image)

cv2.imshow('Original', image)


def mouse_handler(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("left click")
        seed = (x, y)
        cv2.floodFill(image, None, seedPoint=seed, newVal=(0, 0, 255), loDiff=(5, 5, 5, 5), upDiff=(5, 5, 5, 5))
        cv2.imshow("flood", image)


cv2.namedWindow("flood", cv2.WINDOW_AUTOSIZE)
cv2.imshow("flood", image)
cv2.setMouseCallback("flood", mouse_handler)

cv2.waitKey(0)

cv2.destroyAllWindows()

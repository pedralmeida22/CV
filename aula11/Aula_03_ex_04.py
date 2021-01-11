# Aula_03_ex_04.py
#
# Sobel Operator
#
# Paulo Dias - 10/2019


import cv2
import numpy as np
import sys

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

# Sobel Operato3 3 x 3

imageSobel3x3_X = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

cv2.namedWindow("Sobel 3 x 3 - X", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Sobel 3 x 3 - X", imageSobel3x3_X)

image8bits = np.uint8(np.absolute(imageSobel3x3_X))
cv2.imshow("8 bits - Sobel 3 x 3 - X", image8bits)

imageSobel3x3_Y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

cv2.namedWindow("Sobel 3 x 3 - Y", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Sobel 3 x 3 - Y", imageSobel3x3_Y)

image8bits = np.uint8(np.absolute(imageSobel3x3_Y))
cv2.imshow("8 bits - Sobel 3 x 3 - Y", image8bits)

result = imageSobel3x3_X * imageSobel3x3_X + imageSobel3x3_Y * imageSobel3x3_Y
result = np.uint8(np.absolute(result))
cv2.imshow("Result", result)

cv2.waitKey(0)

cv2.destroyAllWindows()

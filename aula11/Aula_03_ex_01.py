# Aula_03_ex_01.py
#
# Mean Filter
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
image = cv2.imread(img2, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be open!")
    exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

# Average filter 3 x 3
imageAFilter3x3_1 = cv2.blur(image, (3, 3))
cv2.imshow("Average Filter 3 x 3 - 1 Iter", imageAFilter3x3_1)

imageAFilter5x5_1 = cv2.blur(image, (5, 5))
cv2.imshow("Average Filter 5 x 5 - 1 Iter", imageAFilter5x5_1)

imageAFilter7x7_1 = cv2.blur(image, (5, 5))
cv2.imshow("Average Filter 7 x 7 - 1 Iter", imageAFilter7x7_1)

imageAFilter3x3_2 = cv2.blur(imageAFilter3x3_1, (3, 3))

imageAFilter3x3_3 = cv2.blur(imageAFilter3x3_2, (3, 3))
cv2.imshow("Average Filter 3 x 3 - 3 Iter", imageAFilter3x3_3)

imageAFilterMedian = cv2.medianBlur(image, 3)
cv2.imshow("Median - 1 Iter", imageAFilterMedian)

imageAFilterGaussian = cv2.GaussianBlur(image, (3,3), 3)
cv2.imshow("Gaussian - 1 Iter", imageAFilterGaussian)


cv2.waitKey(0)

cv2.destroyAllWindows()

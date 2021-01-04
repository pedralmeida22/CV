# import
import numpy as np
import cv2

img2 = "lena.jpg"
img3 = "ireland-06-01.tif"
img = "Fruits-RGB.tif"

# Read the image
image = cv2.imread(img, cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be opened")
    exit(-1)

# Image characteristics
print("Image shape - {}".format(image.shape))
print("Image Type: %s" % image.dtype)

if len(image.shape) < 3:
    height, width = image.shape
    nchannels = 1
else:
    height, width, nchannels = image.shape

imcopy = image.copy()

if nchannels == 1: # gray
    for i in range(0, height, 20):
        cv2.line(imcopy, (i, 0), (i, height), (255))
        cv2.imshow("GRAY", imcopy)

    for i in range(0, width, 20):
        cv2.line(imcopy, (0, i), (width, i), (255))
        cv2.imshow("GRAY", imcopy)

else: # rgb
    for i in range(0, height, 20):
        cv2.line(imcopy, (i, 0), (i, height), (128, 128, 128))
        cv2.imshow("RGB", imcopy)

    for i in range(0, width, 20):
        cv2.line(imcopy, (0, i), (width, i), (128, 128, 128))
        cv2.imshow("RGB", imcopy)


# Create a visualization window
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)

# Show the image
cv2.imshow("Display window", image)

# Wait
cv2.waitKey(0)

# Destroy the window -- might be omitted
cv2.destroyAllWindows()

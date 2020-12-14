# import
import numpy as np
import cv2

# Read the image
# image = cv2.imread("lena.jpg", cv2.IMREAD_UNCHANGED)
image = cv2.imread("Orchid.bmp", cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be opened")
    exit(-1)

# Image characteristics
print("Image shape - {}".format(image.shape))
# height, width = image.shape
height, width, something = image.shape

print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %s" % image.dtype)


def mouse_handler(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("left click")
        center = (x, y)
        radius = 15
        color = (255, 0, 0)
        cv2.circle(image, center, radius, color)
        cv2.imshow("Display window", image)


# Create a visualization window
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback("Display window", mouse_handler)

# Show the image
cv2.imshow("Display window", image)

# Wait
cv2.waitKey(0)

# Destroy the window -- might be omitted
cv2.destroyWindow("Display window")


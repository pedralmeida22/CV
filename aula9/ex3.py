# import
import numpy as np
import cv2

# img1 = "deti.bmp"
# img2 = "deti.jpg"
# img1 = "Calvin.bmp"
# img2 = "Calvin.jpg"
img1 = "Orchid.bmp"
img2 = "Orchid.jpg"

# Read the image
image = cv2.imread(img1, cv2.IMREAD_UNCHANGED)
# image = cv2.imread("Orchid.bmp", cv2.IMREAD_UNCHANGED)

if np.shape(image) == ():
    # Failed Reading
    print("Image file could not be opened")
    exit(-1)

# Image characteristics
height, width, something = image.shape

# Read the image 2
im2 = cv2.imread(img2, cv2.IMREAD_UNCHANGED)
# image = cv2.imread("Orchid.bmp", cv2.IMREAD_UNCHANGED)

if np.shape(im2) == ():
    # Failed Reading
    print("Image file could not be opened")
    exit(-1)

height, width, something = im2.shape

# subtraction
diff_cv = cv2.subtract(image, im2)
diff_np = np.subtract(image, im2)

# Create a visualization window
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow("Display 1 window", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Display 2 window", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Display sub_cv window", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Display sub_np window", cv2.WINDOW_AUTOSIZE)

# Show the image
cv2.imshow("Display 1 window", image)
cv2.imshow("Display 2 window", im2)
cv2.imshow("Display sub_cv window", diff_cv)
cv2.imshow("Display sub_np window", diff_np)

# Wait
cv2.waitKey(0)

# Destroy the window -- might be omitted
cv2.destroyWindow("Display 1 window")
cv2.destroyWindow("Display 2 window")
cv2.destroyWindow("Display sub_cv window")
cv2.destroyWindow("Display sub_np window")
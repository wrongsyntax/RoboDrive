import cv2 as cv
import numpy as np

import filter


NAME = "IMG_0114"

filter.create_mask(NAME)

img = cv.imread(f"./masks/{NAME}_mask.jpeg")
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imwrite("gray.jpeg", grayscale)

# Apply edge detection method on the image
low_thresh = 2
ratio = 76
edges = cv.Canny(grayscale, low_thresh, low_thresh*ratio, apertureSize=3)
# This returns an array of r and theta values
lines = cv.HoughLines(edges, 1, np.pi / 170, 200)

# The below for loop runs till r and theta values
# are in the range of the 2d array
for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    # Stores the value of cos(theta) in a
    a = np.cos(theta)

    # Stores the value of sin(theta) in b
    b = np.sin(theta)

    # x0 stores the value rcos(theta)
    x0 = a * r

    # y0 stores the value rsin(theta)
    y0 = b * r

    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    x1 = int(x0 + 5000 * (-b))

    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
    y1 = int(y0 + 5000 * a)

    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    x2 = int(x0 - 5000 * (-b))

    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
    y2 = int(y0 - 5000 * a)

    # cv.line draws a line in img from the point(x1,y1) to (x2,y2).
    # (0,0,255) denotes the colour of the line to be
    # drawn. In this case, it is red.
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)
    # centre line
    cv.line(img, (img.shape[1]//2, 0), (img.shape[1]//2, 500), (0, 0, 255), 3)

# All the changes made in the input image are finally
# written on a new image houghlines.jpg
cv.imwrite(f"./lines/{NAME}_lines.jpeg", img)

# check which side is offset then compute which way to turns
left_dist = 0
right_dist = 0

for x in range(img.shape[1]//2, 0, -1):
    # print(img[img.shape[0]//2, x])
    if np.array(img[img.shape[0]//2][x] == np.array([255, 255, 255])).all():
        left_dist = img.shape[1]//2 - x
        break

for x in range(img.shape[1]//2, img.shape[1]):
    if np.array(img[img.shape[0]//2][x] == np.array([255, 255, 255])).all():
        right_dist = x - img.shape[1]//2
        break

print(f"{left_dist = }\n{right_dist = }")
        
if left_dist < right_dist:
    print("go right")
else:
    print("go left")

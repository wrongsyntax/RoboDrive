import cv2 as cv
import numpy as np

def create_mask(filename):
    NAME = filename

    img = cv.imread(f"./img/{NAME}.jpeg")

    # convert the BGR image to HSV colour space
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # set the lower and upper bounds for the green hue
    lower_green = np.array([25, 25, 150])
    upper_green = np.array([100, 100, 250])

    # create a mask for green colour using inRange function
    mask = cv.inRange(hsv, lower_green, upper_green)

    # perform bitwise and on the original image arrays using the mask
    res = cv.bitwise_and(img, img, mask=mask)

    # write image to file
    cv.imwrite(f"./masks/{NAME}_mask.jpeg", mask)

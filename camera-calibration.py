import numpy as np
import cv2 as cv
import glob
import os
import pickle

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

across = 4
updown = 4

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((across*updown,3), np.float32)
objp[:,:2] = np.mgrid[0:across,0:updown].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

u = 11
v = 194

images = ['C:\\Users\\sugar\\Desktop\\Projects\\HackED 2023\\Camera Write + Calibration + Undistortion\\frame51.jpg']

for frame in images:
    img = cv.imread(frame)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (across,updown), None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (across,updown), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)

cv.destroyAllWindows()


# Do the calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# img = cv.imread(images[0])
# h,  w = img.shape[:2]
# newmtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))


# undistort
# dst = cv.undistort(img, mtx, dist, None, newmtx)

with open('mtx.pickle', 'wb') as fh:
    pickle.dump(mtx, fh)
with open('dist.pickle', 'wb') as fh:
    pickle.dump(dist, fh)
# with open('newmtx.pickle', 'wb') as fh:
#     pickle.dump(newmtx, fh)
# with open('dst.pickle', 'wb') as fh:
#     pickle.dump(dst, fh)

# crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('_resultant-image.png', dst)
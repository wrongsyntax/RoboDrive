import pickle as pick
import cv2 as cv

def undistort(img_path):
    # get pickle stuffs
    file_mtx = open('mtx.pickle', 'rb')
    mtx = pick.load(file_mtx)

    file_dist = open('dist.pickle', 'rb')
    dist = pick.load(file_dist)
    
    # calibrate the image
    img = img_path
    h,  w = img.shape[:2]
    newmtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

    # undistorting
    und = cv.undistort(img, mtx, dist, None, newmtx)

    # cropping
    x, y, w, h = roi
    und = und[y:y+h, x:x+w]
    # return cv.imshow('image.png', und)
    return cv.imshow('image.png', und)


# undistort("C:\\Users\\sugar\\Desktop\\Projects\\HackED 2023\\Camera Write + Calibration + Undistortion\\Frame51.jpg", mtx, dist)
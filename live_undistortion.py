import undistortion_function as lcu
import cv2   #include opencv library functions in python
import time # include time library functions in python

#Create an object to hold reference to camera video capturing
vidcap = cv2.VideoCapture(0)

#check if connection with camera is successfully
while vidcap.isOpened():
    if vidcap.isOpened():
            ret, frame = vidcap.read()  #capture a frame from live video
            #check whether frame is successfully captured
            if ret:
                # continue to display window until 'q' is pressed
                while(True):
                    cv2.imshow("Frame",frame)   #show captured frame
                    lcu.undistort(frame)
                    # #press 'q' to break out of the loop
                    if cv2.waitKey(1):
                        break
                    time.sleep(1)
                    break
            #print error if frame capturing was unsuccessful
            else:
                print("Error : Failed to capture frame")

        # print error if the connection with camera is unsuccessful

    
    else:
        print("Cannot open camera")

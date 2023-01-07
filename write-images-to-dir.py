import cv2

# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(0)
i = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    # This condition prevents from infinite looping 
    # incase video ends.
    if ret == False:
        break

    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    i += 1

cap.release()
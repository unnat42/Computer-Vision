import cv2
import imutils

cam = cv2.VideoCapture(0)

while True: 
    _,frame = cam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.threshold(blurred,60,100, cv2.THRESH_BINARY_INV)[1]
    
    cv2.imshow("Threshed",thresh)
    
    cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)  #we have the coordinates of the contours with this command

    for c in cnts:
        if cv2.contourArea(c) > 80:
            cv2.drawContours(frame,[c],-1,(0,255,0),3)
            cv2.imshow("Cont",frame)
    	
    key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
    if key == ord("q"):   
        break
cam.release()
cv2.destroyAllWindows()

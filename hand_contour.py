#Had to use 2 different gaussians becuase in the inverse, the hold in between the thumb and index finger wasnt detected
import cv2
import imutils

image = cv2.imread("hand.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blurred, 201,255,cv2.THRESH_BINARY)[1]

#cv2.imshow("Image",image)
#cv2.imshow("Blurred",blurred)
#cv2.imshow("Threshed",thresh)

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  #we have the coordinates of the contours with this command

for c in cnts:
    if cv2.contourArea(c)< 800000:#Gets the hold between the thumb and the index finger
       cv2.drawContours(image,[c],-1,(0,255,0),3)
       cv2.imshow("Hand_1",image)
       
thresh2 = cv2.threshold(blurred,201,255,cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  #we have the coordinates of the contours with this command

for c in cnts:
    if cv2.contourArea(c)> 60: #Gets the rest of the external boundaries of the hand
       cv2.drawContours(image,[c],-1,(0,255,0),3)
       cv2.imshow("Hand_2",image)

#cv2.imwrite("HAND_CONT.jpg",image)
cv2.waitKey(0)



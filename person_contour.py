import cv2
import imutils

image = cv2.imread("person.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blurred,2,255,cv2.THRESH_BINARY)[1]

#cv2.imshow("Threshed",thresh)

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  #we have the coordinates of the contours with this command

for c in cnts:
    if cv2.contourArea(c)> 60: #Gets the rest of the external boundaries of the hand
       cv2.drawContours(image,[c],-1,(255,255,0),3)
       cv2.imshow("Person_Sil",image)

cv2.waitKey(0)
cv2.imwrite("Person_Cont.jpg",image)
cv2.destroyAllWindows()
#Code Courtesy to Adrian from pyimagesearch
#The image to use is also given in the repo

import cv2
import imutils

image = cv2.imread("shapes_and_colors.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blurred, 60,255,cv2.THRESH_BINARY)[1]

#cv2.imshow("Image",image)
#cv2.imshow("Blurred",blurred)
#cv2.imshow("Threshed",thresh)

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  #we have the coordinates of the contours with this command

for c in cnts:
    if cv2.contourArea(c)> 60: #If not used then get a zerodivision error. The threshold value can be anything. Tweak and try
         M = cv2.moments(c)
#    print(c)
         cX = int(M["m10"] / M["m00"])
         cY = int(M["m01"] / M["m00"])
    
    
         cv2.drawContours(image,[c],-1,(0,255,0),2)
         cv2.circle(image,(cX,cY),7,(255,255,255),-1)
         cv2.putText(image,"Center",(cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
    
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    




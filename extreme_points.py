import cv2
import imutils
import numpy as np

image = cv2.imread("hand.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blurred,201,255,cv2.THRESH_BINARY_INV)[1]



thresh = cv2.erode(thresh,None, 2)
thresh = cv2.dilate(thresh, None, 2)



cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)
pts = []

extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

pts.append(extBot)
pts.append(extLeft)
pts.append(extTop)
pts.append(extRight)
pts.append(extBot)
pts = np.array(pts,dtype = int)

cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
cv2.circle(image, extRight, 8, (0, 255, 0), -1)
cv2.circle(image, extTop, 8, (255, 0, 0), -1)
cv2.circle(image, extBot, 8, (255, 255, 0), -1)

cv2.fillConvexPoly(image,pts,(255,0,0),shift=0)
cv2.imshow("Hand",image)
cv2.waitKey(0)
cv2.imwrite("Filled_Fig_Hand.jpg",image)
cv2.destroyAllWindows()
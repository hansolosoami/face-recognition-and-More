#!/usr/bin/env python3

import cv2

#we are taking 3 frames

def imgdiff(x,y,z):
	img1=cv2.absdiff(x,y)   #absdiff---> absolute difference
	img2=cv2.absdiff(y,z)   #absdiff---> absolute difference
	com_diff=cv2.bitwise_and(img1,img2)    #bitwise_and ----> and operation for diff by bit by bit
	return com_diff

cap=cv2.VideoCapture(1)

#taking 3 consistant frames

frame1=cap.read()[1]
frame2=cap.read()[1]
frame3=cap.read()[1]

#converting the frames into greyscale

grey1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
grey2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
grey3=cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)


while cap.isOpened():
		#passing the argument in above function..
		img_diff=imgdiff(grey1,grey2,grey3)
		cv2.imshow('motions are detected',img_diff)
		#capturing  new frames
		status,frame=cap.read()
		grey1=grey2
		grey2=grey3
		grey3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

cv2.destroyAllWindows()
cap.release()


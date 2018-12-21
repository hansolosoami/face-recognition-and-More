#!/usr/bin/env python3

import cv2
import time
cap=cv2.VideoCapture(1)
while cap.isOpened():
	#taking frames
	status,frames=cap.read()
	#extracting only red color
	onlyred=cv2.inRange(frames,(0,0,0),(40,40,255))
	cv2.imshow('only red image ',onlyred)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()


#image masking for color detection project with implementation of region of image(ROI)

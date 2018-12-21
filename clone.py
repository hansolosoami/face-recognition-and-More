#!/usr/bin/env python3

import cv2
import time,copy 
cap=cv2.VideoCapture(1)
i=1
while cap.isOpened():
	#taking frames
	img=cap.read()[1]
	#time.sleep(5)
	cv2.imwrite("image"+str(i)+".jpg",img)
	#extracting the image
	cv2.imshow('the clicked image',img)
	image1=img.copy()
	cv2.imwrite("image1"+str(i)+".jpg",image1)
	time.sleep(1)
	i=i+1	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()

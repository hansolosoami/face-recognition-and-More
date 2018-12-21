#!/usr/bin/python3

import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

cap=cv2.VideoCapture(1)
while True:
	status,frame=cap.read()
	grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(grayimg,1.15,3)
	i=1	
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_cqolor=frame[y:y+h,x:x+w]
		if cv2.waitKey(1) & 0xFF == ord('c'):
			cv2.imwrite('image'+str(i)+'.jpg',roi_color)
			i=i+1
	
	cv2.imshow('image',frame)
	if cv2.waitKey(3) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()	redhat


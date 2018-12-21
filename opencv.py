#!/usr/bin/env python

import cv2

#now starting cam

cap=cv2.VideoCapture(0)

while cap.isOpened():
	print ("camera is working ")
	frame,status=cap.read()
	cv2.imshow('camera1',frame)
	cv2.waitkey(0)

cv2.destroywindow('camera1')
cap.release()

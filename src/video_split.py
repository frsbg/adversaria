import cv2
import os
import sys
import time
import random
import numpy as np

# Read the video from specified path
cam = cv2.VideoCapture("../data/video.mov")

try:
	if not os.path.exists('frames'):
		os.makedirs('frames')

except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0


if __name__=='__main__':
	# reading from frame
	ret,frame = cam.read()

	if ret:
		name = './frames/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name)
		cv2.imwrite(name, frame)
		currentframe += 1

	# make it so that user gives directory of their video and the output is a folder of its image frames rather than any manual input
	cam.release()
	cv2.destroyAllWindows()
	# get estimated time per frame captured to estimate the time to run file for (based on length of video)
	

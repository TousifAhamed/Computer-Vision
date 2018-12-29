import numpy as np
import argparse
import cv2

# Fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array 
image = cv2.imread(args["image"])

# convert the image to grayscale
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#gaussian blurring
blurred = cv2.GaussianBlur(image,(5,5),0)

cv2.imshow("Gaussian Blur", blurred)

#canny detection
canny = cv2.Canny(blurred, 30 ,150)
cv2.imshow("Canny Edge Detected",canny)
cv2.waitKey(0)

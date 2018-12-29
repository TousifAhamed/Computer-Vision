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

cv2.imshow("Gaussian Blurr", blurred)
cv2.waitKey(0)

#simple Thresholding
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

#simple thresholding using inv binart
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary", threshInv)

cv2.imshow("Only Coins", cv2.bitwise_and(image, image, mask = threshInv))


#adaptive thresholding using mean
thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive Mean",thresh)

#adaptive thresholding using gaussian
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive Gaussian",thresh)

cv2.waitKey(0)
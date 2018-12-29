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
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#gaussian blurring
blurred = cv2.GaussianBlur(gray,(27,27),0)

cv2.imshow("Gaussian Blur", blurred)

#canny detection
canny = cv2.Canny(blurred, 30 ,150)
cv2.imshow("Canny Edge Detection", canny)

#finding the contours, counting and marking them
(__,cnts,__) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("The number of coins in the image is : {}".format(len(cnts)))

#create a copy of image
coins = image.copy()

#draw the contours in the actual color image copy
cv2.drawContours(coins, cnts, -1, (0,255,0), 2)
cv2.imshow("Contours", coins)

cv2.waitKey(0)

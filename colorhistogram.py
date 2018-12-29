from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# Fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array 
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

#split image into channels B,G and R

chans = cv2.split(image)

#initialize a tuple 
colors = ("b","g","r")

# set up pyplot figure
plt.figure()
plt.title("Color histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")

for (chan, color) in zip(chans, colors):
	#create the histogram
	hist = cv2.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist)
	plt.xlim([0,256])

plt.show()

cv2.waitKey(0)
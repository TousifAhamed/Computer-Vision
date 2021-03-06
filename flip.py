import argparse
import imutils
import cv2

# Fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array 
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

flipped = cv2.flip(image, 0)
cv2.imshow("Vertical Flip", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, 1)
cv2.imshow("Horizontal Flip", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("Both Flip", flipped)
cv2.waitKey(0)
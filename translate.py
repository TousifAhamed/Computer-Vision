import argparse
import imutils
import cv2

# Fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array
# printing the corresponding values 
image = cv2.imread(args["image"])

# Shif image down
shifted = imutils.translate(image, 0, 50)
cv2.imshow("Shiftd down image", shifted)
cv2.waitKey(0)

# Shif image up
shifted = imutils.translate(image, 0, -50)
cv2.imshow("Shiftd down image", shifted)
cv2.waitKey(0)

# Shif image left
shifted = imutils.translate(image, -50, 0)
cv2.imshow("Shiftd left image", shifted)
cv2.waitKey(0)

# Shif image right
shifted = imutils.translate(image, 50, 0)
cv2.imshow("Shiftd right image", shifted)
cv2.waitKey(0)

# Shif image right and down
shifted = imutils.translate(image, 50, 25)
cv2.imshow("Shiftd right image", shifted)
cv2.waitKey(0)




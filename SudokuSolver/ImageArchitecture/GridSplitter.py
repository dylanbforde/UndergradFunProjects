import cv2 as cv
import numpy as np
import os

image = cv.imread('ImageArchitecture/sudoku_img.png')
# cv.imshow("Image", image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray, (5,5), 0)
#cv.imshow("blur", blur)

thresh = cv.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
#cv.imshow("thresh", thresh)


contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

c = 0
for i in contours:
    area = cv.contourArea(i)
    if area > 1000/2:
        cv.drawContours(image, contours, c, (0, 0, 0), 3)
    c+=1


image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image = cv.bitwise_not(cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 101, 1))

contours, _ = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

c = 0
for i in contours:
    area = cv.contourArea(i)
    if area > 1000:
        cv.drawContours(image, contours, c, (0, 0, 0), 3)
    c+=1

for i, c in enumerate(contours):
    if area > 10000:
        x, y, w, h = cv.boundingRect(c)

        roi = image[y:y+h, x:x+w]
        cv.imwrite(f"ImageOutputs/image_output{i}.jpg", roi)

cv.imshow("Final Image", image)

cv.waitKey(0)
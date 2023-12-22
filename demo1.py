import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Reading in the image
img = cv.imread('stand.jpg')

# Displaying the image
cv.imshow('Stand', img)
cv.waitKey(0)
cv.destroyAllWindows()

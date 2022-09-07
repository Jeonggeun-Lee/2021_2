#Equalization.py

import cv2
import numpy as np
NUM_INTENSITY = 256

def HistogramEqualize(img):
    height, width = img.shape
    num_pixels = height*width

    # making histogram
    histogram = np.zeros((NUM_INTENSITY,))
    for y in range(height):
        for x in range(width):
            histogram[img[y, x]] = histogram[img[y, x]] + 1

    # normalizing histogram
    normalized_histogram = np.divide(histogram, num_pixels)

    # making cdf
    cdf = np.zeros((NUM_INTENSITY,))
    cdf[0] = normalized_histogram[0]
    for k in range(1, NUM_INTENSITY, 1):
        cdf[k] = cdf[k-1] + normalized_histogram[k]

    # finding output gray level
    output_gray_level = np.multiply(NUM_INTENSITY-1, cdf)
    output_gray_level = np.round(output_gray_level)

    # convert image to equalized image
    result = np.zeros((height, width), np.uint8)  # result image
    for y in range(height):
        for x in range(width):
            result[y, x] = output_gray_level[img[y, x]]

    return result


in_image = cv2.imread('dgu_night.png', 0)  # img2numpy

out_image = HistogramEqualize(in_image)

cv2.imshow('Input Image', in_image)
cv2.imshow('Result Image', out_image)

cv2.imwrite('dgu_night_histogram_equalized.png', out_image)  # save result img
cv2.waitKey()

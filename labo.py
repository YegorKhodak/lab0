import cv2
import numpy as np;camera = cv2.VideoCapture(0)

def lab0():
    return_value, image = camera.read()
    cv2.imwrite('opencv.png', image)
    img = cv2.imread('opencv.png')
    cv2.imshow('res', img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]) , (100, 0, 0), 4)
    cv2.rectangle(img, (50, 50), (100, 150), (100, 100, 255), 2)
    cv2.imwrite('opencv.png', img)
    cv2.imshow('res', img)


if __name__ == "__main__":
    lab0()

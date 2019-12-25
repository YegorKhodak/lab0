import cv2
import numpy as np

def lab0():
    camera = cv2.VideoCapture(0)
    ret, image = camera.read()
    cv2.imwrite('cameraShot.png', image)
    camera.release()
    cv2.imshow('img', image)
    image = cv2.imread('cameraShot.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BDR)
    cv2.line(image, (0, 0), (image.shape[1], image.shape[0]) , (100, 0, 0), 5)
    cv2.rectangle(image, (50, 50), (100, 150), (100, 100, 0), 5)
    cv2.imwrite('cameraShot.png', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    lab0()

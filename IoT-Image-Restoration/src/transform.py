import cv2
import numpy as np

def translate(img, x=100, y=50):
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

def rotate(img, angle=45, scale=1.0):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(img, M, (w, h))

def scale(img, fx=0.5, fy=0.5):
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)

def flip(img, mode=1):
    # mode: 1=水平, 0=垂直, -1=双向
    return cv2.flip(img, mode)
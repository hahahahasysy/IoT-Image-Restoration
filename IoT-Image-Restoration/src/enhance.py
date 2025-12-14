import cv2

def histogram_equalization(img):
    """直方图均衡化 (处理灰度)"""
    # 你的原代码是将图转为灰度再均衡化
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.equalizeHist(gray)
    return cv2.equalizeHist(img)
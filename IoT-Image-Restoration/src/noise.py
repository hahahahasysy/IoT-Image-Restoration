import numpy as np
import cv2
import random

def add_gaussian_noise(image, mean=0, sigma=25):
    """
    添加高斯噪声 (源自 demo.py)
    """
    img_float = np.array(image / 255.0, dtype=float)
    noise = np.random.normal(mean, sigma/255.0, img_float.shape)
    out = img_float + noise
    out = np.clip(out, 0.0, 1.0)
    return np.uint8(out * 255)

def add_salt_pepper_noise(image, amount=0.04, salt_vs_pepper=0.5):
    """
    添加椒盐噪声 (源自 demo.py)
    """
    out = np.copy(image)
    # 撒盐 (白点)
    num_salt = np.ceil(amount * image.size * salt_vs_pepper)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[tuple(coords)] = 255

    # 撒胡椒 (黑点)
    num_pepper = np.ceil(amount * image.size * (1.0 - salt_vs_pepper))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[tuple(coords)] = 0
    return out

def generate_motion_psf(shape, angle=20, dist=10):
    """
    生成运动模糊点扩散函数 PSF (源自 图像复原.py)
    """
    h, w = shape[:2]
    psf = np.zeros((h, w), dtype=np.float32)
    center = (w // 2, h // 2)
    
    # 模拟运动模糊 (使用旋转近似直线运动模糊的简化版)
    theta = np.deg2rad(angle)
    num_points = int(dist * 2)
    
    for t in np.linspace(0, theta, num_points):
        x = int(center[0] + dist * np.cos(t))
        y = int(center[1] + dist * np.sin(t))
        if 0 <= x < w and 0 <= y < h:
            psf[y, x] += 1
            
    # 能量归一化
    return psf / psf.sum()
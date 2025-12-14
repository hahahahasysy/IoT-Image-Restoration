import cv2

def apply_denoising_filters(noisy_img):
    """
    应用5种不同的滤波器并返回结果字典 (源自 图像去噪.py)
    """
    results = {}
    
    # 1. 均值滤波
    results['Mean_Blur_3x3'] = cv2.blur(noisy_img, (3, 3))
    
    # 2. 方框滤波
    results['Box_Filter_3x3'] = cv2.boxFilter(noisy_img, -1, (3, 3), normalize=True)
    
    # 3. 高斯滤波
    results['Gaussian_3x3'] = cv2.GaussianBlur(noisy_img, (3, 3), 1.0)
    
    # 4. 中值滤波 (对抗椒盐噪声最佳)
    results['Median_3x3'] = cv2.medianBlur(noisy_img, 3)
    
    # 5. 双边滤波 (保边去噪)
    results['Bilateral'] = cv2.bilateralFilter(noisy_img, d=9, sigmaColor=75, sigmaSpace=75)
    
    return results
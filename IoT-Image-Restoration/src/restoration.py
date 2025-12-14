import numpy as np
import cv2

def inverse_filter_algo(input_img, psf, eps=1e-3):
    """逆滤波核心算法"""
    input_fft = np.fft.fft2(input_img)
    psf_fft = np.fft.fft2(psf) + eps
    result = np.fft.ifft2(input_fft / psf_fft)
    result = np.abs(np.fft.fftshift(result))
    return result

def wiener_filter_algo(input_img, psf, eps, K=0.01):
    """维纳滤波核心算法"""
    input_fft = np.fft.fft2(input_img)
    psf_fft = np.fft.fft2(psf) + eps
    psf_fft_conj = np.conj(psf_fft)
    factor = psf_fft_conj / (np.abs(psf_fft)**2 + K)
    result = np.fft.ifft2(input_fft * factor)
    result = np.abs(np.fft.fftshift(result))
    return result

def restore_image(img, psf, method='wiener', eps=1e-5, K=0.01):
    """
    通用复原接口：支持灰度图和彩色图自动切换
    """
    img_float = img.astype(np.float32)
    
    # 如果是彩色图，拆分通道处理
    if len(img.shape) == 3:
        channels = cv2.split(img_float)
        restored_channels = []
        for chan in channels:
            if method == 'wiener':
                r_chan = wiener_filter_algo(chan, psf, eps, K)
            else:
                r_chan = inverse_filter_algo(chan, psf, eps)
            restored_channels.append(r_chan)
        res = cv2.merge(restored_channels)
    else:
        # 灰度图直接处理
        if method == 'wiener':
            res = wiener_filter_algo(img_float, psf, eps, K)
        else:
            res = inverse_filter_algo(img_float, psf, eps)
        
    # 归一化回 0-255
    res = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX)
    return res.astype(np.uint8)
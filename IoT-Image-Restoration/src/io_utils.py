import cv2
import numpy as np
import os

def read_image(path, color_mode=cv2.IMREAD_COLOR):
    """
    读取图像，支持中文路径 (对应原代码中的 cv2.imdecode)
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"错误：找不到文件 - {path}")
    
    # 使用 imdecode 读取以支持中文路径
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), color_mode)
    return img

def save_image(path, img, ext='.png'):
    """
    保存图像，支持中文路径，自动创建父目录
    """
    dir_name = os.path.dirname(path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    # 确保文件后缀正确
    if not path.endswith(ext):
        path += ext
        
    cv2.imencode(ext, img)[1].tofile(path)
    print(f"[保存成功] {path}")
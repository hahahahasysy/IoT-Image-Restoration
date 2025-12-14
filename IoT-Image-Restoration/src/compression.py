import cv2
import os

def compress_to_size(img, output_path, target_mb=0.5):
    """
    智能压缩：自动调整质量直到文件小于 target_mb
    """
    quality = 95
    while quality > 5:
        # 编码到内存 buffer
        _, buf = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, quality])
        
        # 计算大小 (MB)
        size_mb = len(buf) / (1000 * 1000)
        print(f"尝试压缩质量 {quality}: 大小 = {size_mb:.2f} MB")
        
        if size_mb <= target_mb:
            # 这里的路径处理要注意，因为 buf.tofile 不支持中文路径，
            # 所以我们用 open 写二进制的方式
            with open(output_path, 'wb') as f:
                f.write(buf)
            return True, size_mb
        
        # 衰减策略
        step = 10 if size_mb >= 6.5 else 5
        quality -= step
        
    return False, size_mb
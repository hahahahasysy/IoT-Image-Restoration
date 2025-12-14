import argparse
import os
from src import io_utils, noise, filters, restoration, transform, enhance, compression

def main():
    # 1. 设置命令行参数 - 这让你的程序看起来很像 Linux 工具
    parser = argparse.ArgumentParser(description="IoT Image Restoration Toolkit (Hohai Univ.)")
    
    # 必需参数
    parser.add_argument('--input', type=str, required=True, help='输入图片路径')
    parser.add_argument('--mode', type=str, required=True, 
                        choices=['noise', 'denoise', 'restore', 'transform', 'enhance', 'compress'],
                        help='选择模式: noise(加噪), denoise(去噪), restore(复原), transform(变换)...')
    
    # 可选参数
    parser.add_argument('--output', type=str, default='data/results', help='结果保存目录')
    
    args = parser.parse_args()
    
    # 2. 读取图像 (使用封装好的中文路径读取器)
    try:
        img = io_utils.read_image(args.input)
        filename = os.path.basename(args.input).split('.')[0] # 获取文件名不带后缀
        print(f"成功读取图像: {args.input}, 尺寸: {img.shape}")
    except Exception as e:
        print(f"读取失败: {e}")
        return

    # 3. 模式分发中心
    if args.mode == 'noise':
        # 生成高斯和椒盐噪声
        print(">>> 正在执行：图像加噪...")
        gaussian = noise.add_gaussian_noise(img)
        sp = noise.add_salt_pepper_noise(img)
        
        io_utils.save_image(os.path.join(args.output, f"{filename}_gaussian.png"), gaussian)
        io_utils.save_image(os.path.join(args.output, f"{filename}_salt_pepper.png"), sp)

    elif args.mode == 'denoise':
        # 演示：先加噪，再运行所有滤波器
        print(">>> 正在执行：图像去噪对比...")
        noisy = noise.add_salt_pepper_noise(img, 0.05)
        io_utils.save_image(os.path.join(args.output, f"{filename}_noisy_input.png"), noisy)
        
        results = filters.apply_denoising_filters(noisy)
        for name, res in results.items():
            io_utils.save_image(os.path.join(args.output, f"{filename}_denoise_{name}.png"), res)

    elif args.mode == 'restore':
        # 演示：模拟运动模糊并复原
        print(">>> 正在执行：维纳滤波复原...")
        h, w = img.shape[:2]
        # 生成 PSF
        psf = noise.generate_motion_psf((h, w), angle=20, dist=15)
        
        # 维纳滤波复原 (核心算法)
        restored = restoration.restore_image(img, psf, method='wiener')
        io_utils.save_image(os.path.join(args.output, f"{filename}_restored_wiener.png"), restored)

    elif args.mode == 'transform':
        print(">>> 正在执行：几何变换...")
        rot = transform.rotate(img, angle=45)
        io_utils.save_image(os.path.join(args.output, f"{filename}_rotate_45.png"), rot)

    elif args.mode == 'enhance':
        print(">>> 正在执行：直方图均衡化...")
        res = enhance.histogram_equalization(img)
        io_utils.save_image(os.path.join(args.output, f"{filename}_enhanced.png"), res, ext='.png')

    elif args.mode == 'compress':
        print(">>> 正在执行：智能压缩...")
        out_path = os.path.join(args.output, f"{filename}_compressed.jpg")
        # 确保输出目录存在
        if not os.path.exists(args.output): os.makedirs(args.output)
        
        success, size = compression.compress_to_size(img, out_path, target_mb=0.2) # 压缩到 0.2MB
        if success:
            print(f"压缩完成，最终大小: {size:.2f} MB")

    print(f"\n✅ 所有任务完成！结果已保存在: {args.output}")

if __name__ == '__main__':
    main()
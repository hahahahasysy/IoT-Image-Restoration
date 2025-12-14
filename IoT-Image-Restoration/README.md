# 📷 IoT Visual Perception & Image Restoration Toolkit | 物联网视觉感知与图像复原工具箱

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![University](https://img.shields.io/badge/Hohai-University-red.svg)](https://www.hhu.edu.cn/)

[English](#-english-introduction) | [中文说明](#-项目中文介绍)

---

## 📖 English Introduction

This project, developed at the **College of IoT Engineering, Hohai University**, implements a comprehensive workflow for digital image processing. It is designed to simulate environmental degradation (noise, blur) common in IoT edge devices and applies classical computer vision algorithms to restore signal quality.

Key implementations include **Wiener Filtering** for motion deblurring in the frequency domain and **Bilateral Filtering** for edge-preserving denoising.

### ✨ Key Features

* **⚡ Noise Simulation**:
    * Gaussian Noise (simulating sensor thermal noise).
    * Salt & Pepper Noise (simulating transmission errors).
* **🔍 Advanced Denoising**:
    * Comparative analysis of 5 filters: Mean, Box, Gaussian, Median, and **Bilateral Filter**.
* **🛠 Image Restoration**:
    * **Inverse Filtering**: Basic frequency domain restoration.
    * **Wiener Filtering**: Robust restoration for motion-blurred images minimizing mean square error (MSE).
* **🎨 Enhancement & Compression**:
    * Histogram Equalization for contrast adjustment.
    * Adaptive JPEG compression for bandwidth-constrained IoT transmission.
* **🔄 Geometric Transformations**:
    * Affine operations: Rotation, Translation, Scaling, and Flipping.

### 🚀 Quick Start

```bash
# Clone the repository
git clone [https://github.com/YourUsername/IoT-Image-Restoration.git](https://github.com/YourUsername/IoT-Image-Restoration.git)
cd IoT-Image-Restoration

# Install dependencies
pip install -r requirements.txt

# Run Denoising Demo
python main.py --input data/original/test_image.png --mode denoise





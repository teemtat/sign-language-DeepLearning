#!/usr/bin/env python3
"""
============================================================
Sign Language Deep Learning - Dependency Verification
============================================================
Run this script to verify all dependencies are installed
and working correctly before running the notebooks.

Usage:
    python verify_setup.py
============================================================
"""

import sys
from pathlib import Path

def check_python_version():
    """Check Python version."""
    version = sys.version_info
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("   ⚠️  WARNING: Python 3.10+ recommended")
        return False
    return True

def check_package(package_name, import_name=None):
    """Check if a package is installed and print version."""
    if import_name is None:
        import_name = package_name
    
    try:
        mod = __import__(import_name)
        version = getattr(mod, '__version__', 'unknown')
        print(f"✅ {package_name:<20} v{version}")
        return True
    except ImportError:
        print(f"❌ {package_name:<20} NOT INSTALLED")
        return False

def check_file_exists(filepath, description):
    """Check if a required file exists."""
    if Path(filepath).exists():
        size_mb = Path(filepath).stat().st_size / (1024 * 1024)
        print(f"✅ {description:<30} ({size_mb:.1f} MB)")
        return True
    else:
        print(f"⚠️  {description:<30} not found (will auto-download)")
        return True  # Not critical, can be auto-downloaded

def check_gpu():
    """Check if GPU is available."""
    try:
        import tensorflow as tf
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            for gpu in gpus:
                print(f"✅ GPU detected: {gpu}")
            return True
        else:
            print("ℹ️  No GPU detected (CPU mode - slower but works)")
            return True
    except Exception as e:
        print(f"ℹ️  Could not detect GPU: {e}")
        return True

def check_camera():
    """Check if camera is available."""
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print(f"✅ Camera detected (device 0)")
            cap.release()
            return True
        else:
            print(f"⚠️  Camera not detected at device 0 (try VideoCapture(1) or VideoCapture(2))")
            return True
    except Exception as e:
        print(f"⚠️  Could not check camera: {e}")
        return True

def main():
    print("\n" + "="*60)
    print("Sign Language Deep Learning - Dependency Check")
    print("="*60 + "\n")
    
    all_good = True
    
    # Python version
    print("📌 Python Environment:")
    if not check_python_version():
        all_good = False
    print()
    
    # Core packages
    print("📌 Core Packages:")
    packages = [
        ("NumPy", "numpy"),
        ("Pandas", "pandas"),
        ("Matplotlib", "matplotlib"),
        ("Seaborn", "seaborn"),
        ("Scikit-learn", "sklearn"),
    ]
    for name, import_name in packages:
        if not check_package(name, import_name):
            all_good = False
    print()
    
    # Deep Learning packages
    print("📌 Deep Learning Packages:")
    packages = [
        ("TensorFlow", "tensorflow"),
        ("Keras", "keras"),
    ]
    for name, import_name in packages:
        if not check_package(name, import_name):
            all_good = False
    print()
    
    # Vision packages (critical for camera_detect.ipynb)
    print("📌 Computer Vision Packages (required for camera_detect.ipynb):")
    packages = [
        ("OpenCV", "cv2"),
        ("MediaPipe", "mediapipe"),
    ]
    for name, import_name in packages:
        if not check_package(name, import_name):
            all_good = False
    print()
    
    # Files
    print("📌 Required Files:")
    check_file_exists("Dataset/sign_mnist_train.csv", "Training dataset")
    check_file_exists("Dataset/sign_mnist_test.csv", "Test dataset")
    check_file_exists("outputs/baseline_cnn/best_model.keras", "Baseline CNN model")
    print()
    
    # Hardware
    print("📌 Hardware:")
    check_gpu()
    check_camera()
    print()
    
    # Summary
    print("="*60)
    if all_good:
        print("✅ All dependencies verified! You're ready to run the notebooks.")
        print()
        print("Next steps:")
        print("  1. Open Jupyter Notebook: jupyter notebook")
        print("  2. Start with: main.ipynb → baselineCNN.ipynb → camera_detect.ipynb")
    else:
        print("❌ Some dependencies are missing. Please run:")
        print("   pip install -r requirements.txt")
        print("   pip install opencv-python mediapipe")
        print()
        print("For detailed setup instructions, see README.md")
    print("="*60 + "\n")
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())

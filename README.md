# 📷 Sign Language Deep Learning - Complete Setup Guide

Link to Git hub: https://github.com/teemtat/sign-language-DeepLearning.git

A real-time sign language alphabet (A-Z) detection system using deep learning models trained on the Sign Language MNIST dataset. Features include multiple CNN architectures, transfer learning models, and real-time camera detection using MediaPipe.

---

## 📋 Prerequisites

- **Python**: 3.10 or higher (tested with 3.13.11)
- **Anaconda/Miniconda**: Recommended for environment management
- **Webcam**: Required for `camera_detect.ipynb`
- **OS**: macOS, Linux, or Windows

---

## 🚀 Quick Start

### Step 1: Clone or Download the Repository

```bash
cd /path/to/sign-language-DeepLearning
```

### Step 2: Create Python Environment

We recommend using Conda to isolate dependencies:

```bash
# Create a new conda environment
conda create -n sign-language python=3.11 -y

# Activate the environment
conda activate sign-language
```

**Alternative: Using venv**
```bash
python3 -m venv sign-language-env
source sign-language-env/bin/activate  # On macOS/Linux
# or
sign-language-env\Scripts\activate     # On Windows
```

### Step 3: Install All Dependencies

Install from the provided `requirements.txt` and add critical missing packages:

```bash
pip install -r requirements.txt
pip install opencv-python mediapipe
```

**Full dependency list:**
```
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.2.0
tensorflow>=2.13.0
tensorboard>=2.13.0
opencv-python>=4.8.0
mediapipe>=0.10.0
```

### Step 4: Download MediaPipe Hand Landmarker Model

The `camera_detect.ipynb` automatically downloads this ~2 MB model on first run. No manual download needed!

The notebook will download it from:
```
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
```

---

## 📂 Project Structure

```
sign-language-DeepLearning/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── hand_landmarker.task               # MediaPipe model (auto-downloaded)
│
├── 📔 NOTEBOOKS:
├── main.ipynb                         # EDA & data exploration
├── baselineCNN.ipynb                  # Train baseline CNN model
├── camera_detect.ipynb                # ⭐ Real-time detection (requires webcam)
├── experiment_models.ipynb            # Test multiple architectures
│
├── Dataset/
│   ├── sign_mnist_train.csv          # Training data (27,455 samples)
│   ├── sign_mnist_test.csv           # Test data (7,172 samples)
│   ├── sign_mnist_train/
│   │   └── sign_mnist_train.csv
│   └── sign_mnist_test/
│       └── sign_mnist_test.csv
│
├── outputs/                           # Trained models (saved as .keras)
│   ├── baseline_cnn/best_model.keras
│   ├── depthwise_cnn/best_model.keras
│   ├── inception_cnn/best_model.keras
│   ├── residual_cnn/best_model.keras
│   └── se_cnn/best_model.keras
│
└── logs/                              # TensorBoard training logs
    ├── baseline_cnn/
    ├── depthwise_cnn/
    ├── inception_cnn/
    ├── residual_cnn/
    └── se_cnn/
```

---

## 📔 Notebook Guide

### 1️⃣ **main.ipynb** — EDA & Data Exploration
- Load and explore the Sign Language MNIST dataset
- Visualize class distribution and sample images
- Check for missing values and duplicates
- **Dependencies**: pandas, numpy, matplotlib
- **Run time**: ~2 minutes
- **Prerequisites**: None (data included)

### 2️⃣ **baselineCNN.ipynb** — Train Baseline Model
- Build and train a simple CNN classifier
- Train/validation/test split
- Plot accuracy, loss, and confusion matrix
- Save best model to `outputs/baseline_cnn/best_model.keras`
- **Dependencies**: tensorflow, keras, scikit-learn, matplotlib
- **Run time**: ~20-30 minutes (GPU: ~5-10 minutes)
- **Prerequisites**: main.ipynb (recommended but optional)

### 3️⃣ **experiment_models.ipynb** — Compare Multiple Architectures
- Train 5 different CNN models (Baseline, Depthwise, Inception, Residual, SE-Net)
- Compare performance across architectures
- Generate gridsearch results CSVs
- **Dependencies**: tensorflow, keras, scikit-learn
- **Run time**: ~2-3 hours (GPU: ~30-45 minutes)
- **Prerequisites**: baselineCNN.ipynb (recommmended)

### 4️⃣ **camera_detect.ipynb** — Real-Time Detection ⭐
The star of the show! Real-time sign language detection through your webcam.

**Features:**
- Uses `outputs/baseline_cnn/best_model.keras` for predictions
- MediaPipe hand detection & tracking
- Real-time preprocessing with CLAHE contrast enhancement
- Confidence thresholding (60% by default)
- Smoothed predictions using sliding window voting
- ROI preview in bottom-right corner

**How to use:**
1. Run all cells in order
2. Allow camera access when prompted
3. Raise your hand in front of the camera (in the green box)
4. Press `q` to quit the camera

**Dependencies**: tensorflow, opencv-python, mediapipe, numpy
**Run time**: ~2 minutes setup + continuous real-time detection
**Prerequisites**: 
  - `outputs/baseline_cnn/best_model.keras` (trained model file)
  - Webcam/camera device
  - MediaPipe model (auto-downloaded on first run)

**Troubleshooting camera_detect.ipynb:**
- **"Cannot open camera"**: Try changing `VideoCapture(0)` to `VideoCapture(1)` or `VideoCapture(2)`
- **Slow predictions**: Reduce model input size or disable CLAHE preprocessing
- **Inaccurate predictions**: Ensure good lighting; increase `CONFIDENCE` threshold

---

## 🔧 Dependency Summary

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | ≥1.24.0 | Numerical computing |
| pandas | ≥2.0.0 | Data manipulation |
| matplotlib | ≥3.7.0 | Plotting & visualization |
| seaborn | ≥0.12.0 | Statistical visualization |
| scikit-learn | ≥1.2.0 | ML metrics & preprocessing |
| **tensorflow** | ≥2.13.0 | Deep learning framework |
| tensorboard | ≥2.13.0 | Training visualization |
| **opencv-python** | ≥4.8.0 | Computer vision (required for camera) |
| **mediapipe** | ≥0.10.0 | Hand detection (required for real-time) |

**Bold packages** are critical and often missing from basic installations.

---

## ⚡ Common Installation Issues

### Issue: "No module named 'cv2'"
**Solution:**
```bash
pip install opencv-python
```

### Issue: "No module named 'mediapipe'"
**Solution:**
```bash
pip install mediapipe
```

### Issue: Camera detection fails with "Cannot open camera"
**Solutions:**
1. Try different camera indices: `VideoCapture(1)` or `VideoCapture(2)`
2. Check camera permissions on macOS: System Preferences → Security → Camera
3. Ensure no other application is using the camera

### Issue: Slow notebook execution or GPU not detected
**Check GPU:**
```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

**Install TensorFlow with GPU support:**
```bash
# For NVIDIA GPUs (CUDA)
pip install tensorflow[and-cuda]

# For macOS with Apple Silicon (Metal)
conda install -c conda-forge tensorflow-metal
```

### Issue: Models not found in outputs folder
**Solution:**
Run `baselineCNN.ipynb` first to train and save models:
```bash
jupyter notebook baselineCNN.ipynb
```

---

## 🎯 Recommended Workflow

**For first-time users:**
1. ✅ Activate environment and install dependencies
2. ✅ Run `main.ipynb` (quick data exploration)
3. ✅ Run `baselineCNN.ipynb` (train model if needed)
4. ✅ Run `camera_detect.ipynb` (real-time detection)

**For model experimentation:**
1. ✅ Run `experiment_models.ipynb` to train multiple models
2. ✅ Modify `MODEL_PATH` in `camera_detect.ipynb` to test different models
3. ✅ Compare gridsearch results (CSVs in root directory)

---

## 📊 Trained Models

All trained models are pre-saved in the `outputs/` folder:

| Model | Path | Accuracy | Architecture |
|-------|------|----------|--------------|
| Baseline CNN | `outputs/baseline_cnn/best_model.keras` | ~95% | 3-layer CNN |
| Depthwise CNN | `outputs/depthwise_cnn/best_model.keras` | ~94% | Depthwise separable |
| Inception CNN | `outputs/inception_cnn/best_model.keras` | ~96% | Inception blocks |
| Residual CNN | `outputs/residual_cnn/best_model.keras` | ~96% | ResNet-style |
| SE-Net CNN | `outputs/se_cnn/best_model.keras` | ~95% | Squeeze-Excitation |

---

## 🎓 Dataset Info

**Sign Language MNIST**
- **Source**: Kaggle (https://www.kaggle.com/datasets/datamunge/sign-language-mnist)
- **Classes**: 24 (A-Z excluding J and Z, which require motion)
- **Training samples**: 27,455 images
- **Test samples**: 7,172 images
- **Image size**: 28×28 pixels (grayscale)
- **Format**: CSV with label + 784 pixel values

---

## 💻 Environment Configuration

If you need to check your current environment:

```python
import sys
import numpy as np
import tensorflow as tf
import cv2
import mediapipe as mp

print(f"Python: {sys.version}")
print(f"NumPy: {np.__version__}")
print(f"TensorFlow: {tf.__version__}")
print(f"OpenCV: {cv2.__version__}")
print(f"MediaPipe: {mp.__version__}")
```

Or from terminal:
```bash
python -c "import sys; print(f'Python {sys.version}')"
pip list  # Show all installed packages
```

---

## 📝 Notes for Running on Different Devices

### macOS
- ✅ Works with native camera
- ⚡ For Apple Silicon Macs (M1/M2/M3): Install TensorFlow Metal for GPU acceleration
  ```bash
  conda install -c conda-forge tensorflow-metal
  ```

### Linux
- ✅ Install OpenCV system dependency if needed:
  ```bash
  sudo apt-get install libsm6 libxext6 libxrender-dev  # Ubuntu/Debian
  ```

### Windows
- ✅ Use Anaconda Prompt instead of terminal
- ✅ Camera index may differ (try 0, 1, 2)
- ⚡ NVIDIA GPU support with CUDA:
  ```bash
  pip install tensorflow[and-cuda]
  ```

---

## 🤝 Troubleshooting Checklist

Before running notebooks, verify:
- [ ] Conda/venv environment activated
- [ ] All packages installed: `pip list` shows opencv-python and mediapipe
- [ ] Dataset files exist in `Dataset/` folder
- [ ] `hand_landmarker.task` will auto-download
- [ ] GPU detected (optional): `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

If camera_detect.ipynb fails:
- [ ] Camera works in other apps (Photo Booth, etc.)
- [ ] Try `VideoCapture(1)` or `VideoCapture(2)`
- [ ] Check camera permissions (macOS: System Preferences → Security)
- [ ] Ensure good lighting and hand visibility
- [ ] Model file exists: `ls outputs/baseline_cnn/best_model.keras`

---

## 📞 Support

If your friend still can't run the code after following this guide:

1. **Share your environment:**
   ```bash
   conda env export > environment.yml
   # Share environment.yml with your friend
   
   # Friend's machine:
   conda env create -f environment.yml
   conda activate sign-language
   ```

2. **Verify dependencies:**
   ```bash
   pip install -r requirements.txt --upgrade
   pip install opencv-python mediapipe --upgrade
   ```

3. **Test imports:**
   ```python
   python -c "import cv2, mediapipe, tensorflow; print('All packages loaded successfully!')"
   ```

---

## 📄 License & Attribution

- **Dataset**: Sign Language MNIST from Kaggle (CC0)
- **MediaPipe**: Google (Apache 2.0)
- **TensorFlow**: Google (Apache 2.0)

---

**Last Updated**: April 2026  
**Python Version**: 3.10+  
**Tested On**: macOS (Apple Silicon & Intel), Linux

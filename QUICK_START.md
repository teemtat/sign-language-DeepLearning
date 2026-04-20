# ⚡ Quick Start - Camera Detection (5 Minutes)

If you just want to run `camera_detect.ipynb` and see real-time sign language detection, follow this:

## 🎯 The Absolute Fastest Path

### 1. Open Terminal/Command Prompt

### 2. Navigate to the project folder
```bash
cd /path/to/sign-language-DeepLearning
```

### 3. Create environment (one-time only)
```bash
# macOS/Linux
conda create -n sign-language python=3.11 -y
conda activate sign-language

# Windows
conda create -n sign-language python=3.11 -y
conda activate sign-language
```

### 4. Install everything
```bash
pip install -r requirements.txt
```

### 5. Verify setup
```bash
python verify_setup.py
```

You should see green ✅ checkmarks next to all packages.

### 6. Open Jupyter & Run camera_detect.ipynb
```bash
jupyter notebook
```

Then:
- Click on `camera_detect.ipynb`
- Press "Run All" or press `Shift + Enter` for each cell
- Allow camera access when prompted
- Raise your hand to the camera!
- Press `q` to quit

---

## 🆘 If It Still Doesn't Work

### "Module not found" errors?
```bash
# Make sure you're in the right environment
conda activate sign-language

# Reinstall everything
pip install --upgrade -r requirements.txt
```

### Camera won't open?
In `camera_detect.ipynb`, find the line with `VideoCapture(0)` and try:
```python
# Try these one at a time:
cap = cv2.VideoCapture(0)  # Try this first
cap = cv2.VideoCapture(1)  # If 0 doesn't work
cap = cv2.VideoCapture(2)  # If 1 doesn't work
```

### Missing model file?
The file `outputs/baseline_cnn/best_model.keras` must exist. If not:
```bash
# Option 1: Download from the repo
git clone <repo-url>

# Option 2: Train the model yourself
# Run: baselineCNN.ipynb (takes ~20 min on CPU, ~5 min on GPU)
```

### Still stuck?
1. Run `python verify_setup.py` and share the output
2. Check README.md for detailed troubleshooting
3. Make sure you're using the right Python environment: `which python` (should show conda path)

---

## 📋 Minimum Requirements Checklist

- [ ] Python 3.10+ installed
- [ ] Conda/Miniconda installed  
- [ ] `requirements.txt` file exists
- [ ] Webcam/camera connected
- [ ] Good lighting where you'll be using the camera
- [ ] ~5 GB free disk space (for model files, datasets)

---

## ✅ You'll Know It's Working When:

1. Terminal shows no error messages after `pip install -r requirements.txt`
2. `python verify_setup.py` shows all ✅ green checkmarks
3. `camera_detect.ipynb` opens in Jupyter without errors
4. Camera window appears after running all cells
5. Your hand appears in the green box with a predicted letter above it

---

**Pro Tip**: First time takes 15-20 minutes to download and install. After that, it's instant—just `conda activate sign-language` and `jupyter notebook`.

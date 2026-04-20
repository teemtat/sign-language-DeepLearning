#!/bin/bash
# ============================================================
# Sign Language Deep Learning - Automated Setup Script
# ============================================================
# This script creates a conda environment and installs all
# dependencies needed to run the notebooks.
#
# Usage:
#   chmod +x setup.sh
#   ./setup.sh
#
# For Windows: Use setup.bat or follow manual steps in README.md
# ============================================================

set -e  # Exit on any error

echo "🚀 Sign Language Deep Learning - Environment Setup"
echo "=================================================="

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ ERROR: Conda not found!"
    echo "Please install Anaconda or Miniconda first:"
    echo "   https://www.conda.io/projects/conda/en/latest/user-guide/install/"
    exit 1
fi

ENV_NAME="sign-language"

echo ""
echo "📦 Step 1: Creating conda environment '$ENV_NAME' with Python 3.11..."
conda create -n "$ENV_NAME" python=3.11 -y

echo ""
echo "🔧 Step 2: Activating environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate "$ENV_NAME"

echo ""
echo "📚 Step 3: Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ SETUP COMPLETE!"
echo ""
echo "📝 Next steps:"
echo "   1. Activate the environment:"
echo "      conda activate $ENV_NAME"
echo ""
echo "   2. Open Jupyter Notebook:"
echo "      jupyter notebook"
echo ""
echo "   3. Start with: main.ipynb → baselineCNN.ipynb → camera_detect.ipynb"
echo ""
echo "For more details, see README.md"

FROM --platform=linux/arm64 python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir \
    tensorflow==2.16.1 \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    opencv-python-headless \
    jupyterlab \
    ipywidgets

COPY . .

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]

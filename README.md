# HAM10000 Dataset Classification Challenge

## Introduction

This repository contains Jupyter notebook scripts for training machine learning models for HAM10000 Dataset

### Machine Learning Models

The repository contains implementations of various state-of-the-art machine learning models designed for image classification tasks. These models are trained and evaluated on the HAM10000 dataset, which consists of dermatoscopic images of different types of skin lesions. The included models are:

- **EfficientNet**: A family of convolutional neural networks (CNNs) known for achieving high accuracy while being computationally efficient. EfficientNet models scale up in a balanced manner across depth, width, and resolution.
  
- **Vision Transformer (ViT)**: A transformer-based architecture that applies the transformer model directly to sequences of image patches. It leverages the power of self-attention mechanisms, traditionally used in natural language processing, for image classification tasks.
  
- **ConvNextBase**: A modernized version of the standard CNN architecture that incorporates advances from recent research, such as normalization, depth-wise convolutions, and residual connections, to achieve superior performance.
  
- **Custom CNN**: A tailored convolutional neural network designed specifically for the HAM10000 dataset. This model serves as a baseline to compare with the more complex architectures like EfficientNet, ViT, and ConvNextBase.

Each of these models has been implemented and tested in the provided notebooks, with detailed steps for data handling, data exploration, and model evaluation.


## Contents

The repository includes the following notebooks:

- **Model.ipynb**: Notebook implementing Data Handling, Data Exploration and Model testing for the created models which include EfficientNet, Vision Transformer, ConvNextBase and CNN model architectures. 
- **Requirements.py**: Python file which helps install the required dependencies.


## Dependencies

The scripts require the following dependencies:

- Python 3.x
- PyTorch
- NumPy
- Matplotlib
- torchvision
- torchsummary
- PIL
- Pandas
- sklearn
- efficientnet_pytorch

You can install the required packages using the below in terminal:

```bash
python requirements.py

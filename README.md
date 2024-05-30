# Model Inversion and Part Classification

## Introduction

This repository contains Jupyter notebook scripts for training machine learning models for HAM10000 Dataset

### Model Inversion

Model inversion is a type of attack where an adversary attempts to reconstruct sensitive input data based on the output of a machine learning model. In this project, we explore model inversion attacks in the context of a part classifier model trained on casting images.

## Notebooks

The repository includes the following notebooks:

- **Model_Inversion_split_layer_2.ipynb**: Notebook implementing the part classifier model with a split layer setting of 2.
- **Model_Inversion_split_layer_3.ipynb**: Notebook implementing the part classifier model with a split layer setting of 3.
- **Model_Inversion_split_layer_4.ipynb**: Notebook implementing the part classifier model with a split layer setting of 4.
- **Model_Inversion_split_layer_6.ipynb**: Notebook implementing the part classifier model with a split layer setting of 6.
- **Model_Inversion_split_layer_8.ipynb**: Notebook implementing the part classifier model with a split layer setting of 8.

Each notebook explores the impact of different split layer settings on model performance and vulnerability to model inversion attacks.

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

You can install the required packages using pip:

```bash
pip install torch numpy matplotlib torchvision torchsummary Pillow

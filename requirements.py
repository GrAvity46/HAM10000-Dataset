import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_dependencies():
    dependencies = [
        "torch",
        "torchvision",
        "numpy",
        "matplotlib",
        "pillow",
        "pandas",
        "scikit-learn",
        "efficientnet_pytorch",
        "torchsummary"
    ]
    
    for package in dependencies:
        install(package)

if __name__ == "__main__":
    install_dependencies()

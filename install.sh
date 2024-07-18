conda deactivate

# Set environment variables
export ENV_NAME=yolov8 # Choose ur own virtual env name
export PYTHON_VERSION=3.9

# Create a new conda environment and activate it
conda create -n $ENV_NAME python=$PYTHON_VERSION
conda activate $ENV_NAME

# Install PyTorch, torchvision, and PyTorch3D using conda
conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=12.1 -c pytorch -c nvidia

## Macbook using:
#pip install torch torchvision torchaudio

# Install ultralytics for pretrained yolov8 model
pip install ultralytics

# Other packages to manage data
pip install pandas sqlalchemy

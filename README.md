![NurSecure](https://imgur.com/3RoCeZT.png)

# NurSecure
NurSecure is an machine-learning powered chatbot that can analyze descriptions, classify syndrome and point you directly to the specialist.

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Setup

### Python package
Required evironment: MacOS, Linux
With miniconda/anaconda (recomended):
```bash
conda create python=3.6 -n NurSecure
source activate NurSecure
pip install -r requirements.txt
```
Without miniconda/anaconda:
```bash
pip install -r requirements.txt
```

### AWS

pip install awscli

```bash
aws configure --profile nursecure
# Default region name [None]: us-east-1
# Default output format [None]: json
```

## Usage
```
python NurSecure
```

## Useful Links
[15 Good Datasets](https://gengo.ai/datasets/15-best-chatbot-datasets-for-machine-learning/)
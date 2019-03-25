![NurSecure](https://imgur.com/3RoCeZT.png)

# NurSecure
NurSecure is a simple, rule-based chatbot that analyzes descriptions, classifies syndrome and points you directly to the specialist.  

__Work in progress!!!__

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Setup

### Python package
Required evironment: MacOS, Linux

#### With miniconda/anaconda (recomended)

```bash
conda create python=3.6 -n NurSecure
source activate NurSecure
pip install -r requirements.txt
```

#### Without miniconda/anaconda

```bash
pip install -r requirements.txt
```

### AWS

```bash
pip install awscli
aws configure --profile nursecure
# Default region name [None]: us-east-1
# Default output format [None]: json
```

#### IAM settings
```json
{
    "Effect": "Allow",
    "Action": "comprehendmedical:*",
    "Resource": "*"
}
```

## Usage

```
python -m NurSecure
```

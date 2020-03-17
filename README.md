<p align="left">
  <img src="https://github.com/X-ray-Dawgz/XRayDawgz/blob/master/banner.png" width="900">
</p>


[![Build Status](https://travis-ci.com/X-ray-Dawgz/XRayDawgz.svg?branch=master)](https://travis-ci.com/X-ray-Dawgz/XRayDawgz)
[![Coverage Status](https://coveralls.io/repos/github/X-ray-Dawgz/XRayDawgz/badge.svg?branch=master)](https://coveralls.io/github/X-ray-Dawgz/XRayDawgz?branch=master)
- UW DIRECT project of a general XRD image pattern classifier framework for predicting crystal structure.

## Table of Contents
- Purpose
- How to install
- Environment
- Examples and Demos
- How to use our software
- License

## Repository Structure 
```
  |- README.md
  |- Images/
      |- BCC_test
      |- BCC_train
      |- Cubic_BCC
      |- Cubic_FCC
      |- FCC_test
      |- FCC_train
  |- XRayDawgz/
      |- __init__.py
      |- core.py
      |- version.py
      |- ROILocator.py
      |- tests/
        |- __init__.py
        |- test_core.py
        |- cut_image/
          |- Test/
          |- Train/
      |- data/
        |- July_test.tif
        |- test_ROI.tif
        |- test_gray.tif
      |- __pycache__/
  |- docs/
      |- Tech_review.pdf
      |- functional_spec.md
      |- component_spec.md
  |- setup.py
  |- .travis.yml
  |- .coveragerc
  |- .coverage.yml
  |- environment.yml
  |- .gitignore
  |- LICENSE 
  |- banner.png
  |- requirements.txt
 ``` 
  
## Purpose
This project will aim to use CNN to predict the crystal structure of a sample based upon its XRD pattern.

## How to install
1. install tensorflow 
`conda install tensorflow`
2. more detail...

## Examples and Demos


## How to use our software

## License
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

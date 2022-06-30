# Breast Cancer Diagnosis by Causal_inference

![lidar-heatmap](bc.jpg)

**Table of content**

- [Overview](#overview)
- [Install](#install)
- [Data](#data)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Test](#test)

## Introduction

> Breast-cancer Diagnostic The second greatest cause of cancer death in women, after lung cancer, is breast cancer, which is the most prevalent invasive cancer in females. Since 1989, significant progress has been made in the detection and treatment of breast cancer. More than 3.1 million Americans have survived breast cancer, according to the American Cancer Society (ACS). About 1 in 38 women will develop breast cancer in their lifetime (2.6 percent ). Early detection of the disease and precise diagnosis both increase the likelihood of long-term survival for a person with breast cancer.The prognosis, or anticipated long-term behavior of the disease, heavily influences the choice of appropriate therapy immediately following surgery.
The purpose of this project is to extract useful features by using causal inferences and building the model to predict the diagnosis.

# Overview

> The purpose of this project is to extract useful features by using causal inferences and building the model to predict the diagnosis. The causal graph is a central object in the framework mentioned above, but it is often unknown, subject to personal knowledge and bias, or loosely connected to the available data. The main objective of the task is to highlight the importance of the matter in a concrete way. In this spirit, trainees are expected to attempt the following tasks:

            Perform a causal inference task using Pearl’s framework
            Infer the causal graph from observational data and then validate the graph
            Merge machine learning with causal inference



## Install

```bash
git clone https://github.com/Ammon21/Causal-Inference.git
cd Causal-Inference
sudo python3 setup.py install
```

<hr>

## Data

 > I extracted the data from kaggle. i downloaded and put it in my repository data folder. i was  provided with a csv file with 31 features including the target variable diagnosis. Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

## [notebooks](notebooks):

- `notebooks`: a jupyter notebook for preprocessing the data.

## [scripts](scripts):

- `scripts/`: folder where modules are stored. 

## [tests](tests):

- `tests/`: the folder containing unit tests for the scripts.



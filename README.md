# GymEquiptmentClassifier
**Project by Andrew Bonafede Duke AIPI 540**

## Project Description

## Project Structure
The project data and codes are arranged in the following manner:

```
├── README.md                           <- description of project and how to set up and run it
├── requirements.txt                    <- requirements file to document dependencies
├── scripts                             <- directory for data processing, modelling and utility scripts
    ├── evaluation                      <- script to evaluate different models
        ├── eval_config.json
        ├── eval.py
        ├── eval_helper_functions.py
    ├── resnet                          <- script to train and test the resnet model
        ├── resnet_config.json
        ├── resnet_helper_functions.py
        ├── resnet_transfer_learning.py
    ├── svm                             <- script to train and test the svm model
        ├── svm_config.json
        ├── svm_helper_functions.py
        ├── svm_training.py.py
├── models                              <- directory for trained models
├── data                                <- directory for project data 
    ├── barbell
    ├── bench
    ├── dumbell
    ├── kettlebell
    ├── rack
├── scratch                             <- directory to store any intermediate and scratch files used
├── notebooks                           <- directory to store any exploration notebooks used
├── .gitignore                          <- git ignore file
```

&nbsp;
## Model Training and Evaluation

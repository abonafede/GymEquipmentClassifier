# GymEquiptmentClassifier
**Project by Andrew Bonafede Duke AIPI 540**

## Project Description
Our computer vision system is designed to help gym-goers maximize their workouts by identifying the gym equipment available and suggesting exercises that can be performed using that equipment. Whether you're a beginner who is unfamiliar with the different types of gym equipment or a regular gym-goer who is frustrated by not being able to use your preferred equipment due to high demand, our system can help you get the most out of your gym experience. Simply upload a photo of the gym equipment you want to use, and our system will classify it and provide you with a list of exercises that can be performed using that equipment.

Our system is designed to be easy to use, with a user-friendly interface that allows you to quickly and easily upload photos and access suggested exercises. In addition to identifying gym equipment and suggesting exercises, our system also provides detailed instructions and videos for each exercise, ensuring that you can perform them safely and effectively. Our goal is to empower gym-goers of all skill levels to take control of their workouts and achieve their fitness goals. Whether you're a beginner or an experienced gym-goer, our computer vision system can help you get the most out of your gym experience.

### The Data
Our computer vision system uses a dataset of gym equipment images to classify the equipment and suggest exercises that can be performed using them. The dataset consists of five classes: dumbbell, barbell, kettlebell, bench, and squat rack. Each class contains approximately 2000 images, with 200 images of each class being made available on git. The full dataset is available upon request by contacting abonafede5@gmail.com. The images in the dataset were collected from various sources, including stock image websites and personal gym photos, and were carefully selected to ensure a diverse range of lighting conditions, angles, and equipment variations. The images were labeled manually by expert gym-goers to ensure accuracy and consistency in the classification of gym equipment. With this dataset, our computer vision system is able to accurately classify gym equipment and provide users with suggested exercises for each piece of equipment.

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
├── notebooks                           <- directory to store any exploration notebooks used
├── .gitignore                          <- git ignore file
```

&nbsp;
## Model Training and Evaluation

### SVM
Following are the steps to run the code and train a SVM model:

**1. Create a new conda environment and activate it:** 
```
conda create --name cv python=3.8
conda activate cv
```
**2. Install python package requirements:** 
```
pip install -r requirements.txt 
```

**3. Tweak the model parameters [OPTIONAL]:** 
```
nano scripts/svm/svm_config.json
```

**4. Run the training script:** 
```
python scripts/svm/svm_training.py
```
&nbsp;

### Deep Learning
Available models to train:
- Resnet18 with all layers trainable
- Resnet18 with just the last fully connected layer trainable
- Resnet50 with all layers trainable
- Resnet50 with just the last fully connected layer trainable
- Resnet152 with all layers trainable
- Resnet152 with just the last fully connected layer trainable

The default is Resnet 152 wih just the last fully connected layer trainable.

Following are the steps to run the code and train a Resnet model:

**1. Create a new conda environment and activate it:** 
```
conda create --name cv python=3.8
conda activate cv
```
**2. Install python package requirements:** 
```
pip install -r requirements.txt 
```

**3. Tweak the model parameters [OPTIONAL]:** 
```
nano scripts/resnet/resnet_config.json
```

**4. Run the training script:** 
```
python scripts/resnet/resnet_transfer_learning.py
```
&nbsp;
## Gym Equipment Classifier Application (Streamlit):
Currently hosted on Google Cloud Platform publicly available at https://caramel-spot-384823.ue.r.appspot.com/
If not, the app can be run locally in the st branch of this repo.
See details of how to run locally [here](https://github.com/abonafede/GymEquipmentClassifier/blob/st/README.md)
Find the source code [here](https://github.com/abonafede/GymEquipmentClassifier/tree/st)
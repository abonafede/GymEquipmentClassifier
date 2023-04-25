# GymEquiptmentClassifier

**Project by Andrew Bonafede for Duke AIPI 540**

## Gym Equipment Classifier (Streamlit App):
A streamlit based web application which provides you the ability to upload an image of your gym equipment. The model will infer which equipment you have and display to you a list of workouts involving said equipment. It also includes a dummy recommendation to be updated soon.

&nbsp;
## Running the Code

**1. Clone the repository**
```
git clone https://github.com/abonafede/GymEquipmentClassifier.git
```
**2. Switch to the 'st' branch**
```
git checkout st
```
**3. Create a conda environment and activate it:** 
```
conda create --name st_env python=3.9
conda activate st_env
```
**4. Install requirements:** 
```
pip install -r requirements.txt
```
**5. Run the application**
```
streamlit run home.py
```
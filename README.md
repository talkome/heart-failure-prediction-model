# Heart Failure Prediction Model

## Introduction
- Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. 
- Four out of 5 CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. 
- Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease. 
- People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.


## Features

- Quick Answer. 
- Base on relevant medical parameters.
- Use neural network for learning and predicting cardiovascular diseases.

## Attributions

- *Age*: age of the patient [years]
- *Sex*: sex of the patient [M: Male, F: Female]
- *ChestPainType*: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
- *RestingBP*: resting blood pressure [mm Hg]
- *Cholesterol*: serum cholesterol [mm/dl]
- *FastingBS*: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
- *RestingECG*: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
- *MaxHR*: maximum heart rate achieved [Numeric value between 60 and 202]
- *ExerciseAngina*: exercise-induced angina [Y: Yes, N: No]
- *Oldpeak*: oldpeak = ST [Numeric value measured in depression]
- *ST_Slope*: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
- *HeartDisease*: output class [½  < : heart disease, ½ > : Normal]

## Install

This project requires Python 3 and the following Python libraries installed:

- Flask~=2.0.3
- pandas~=1.1.5
- torch~=1.10.2
- scikit-learn~=0.24.2
- gunicorn~=19.9.0
- Flask-Cors~=3.0.10

## Preview

![WhatsApp Image 2022-08-17 at 9 41 28 PM](https://user-images.githubusercontent.com/52321544/185230281-4dcbd9c7-eafb-4fbd-874d-c4f5f1282989.jpeg)

![WhatsApp Image 2022-08-17 at 9 41 28 PM](https://user-images.githubusercontent.com/52321544/185230415-fde4ade0-2d6a-483d-97a1-fc9a5efdf55c.jpeg)


## Project flowchart:

![1](https://user-images.githubusercontent.com/10403994/185229861-0766a960-22ea-461e-b365-d1c833adda1d.jpg)



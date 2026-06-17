# Exploratory Data Analysis Findings

## Dataset Overview

* Dataset Size: 10,000 records
* Features: 6 clinical predictors
* Target: Diagnosis (Endometriosis)

## Features

1. Age
2. Menstrual Irregularity
3. Chronic Pain Level
4. Hormone Level Abnormality
5. Infertility
6. BMI

## Missing Values

No missing values were detected.

## Class Distribution

* Negative Diagnosis: 59.21%
* Positive Diagnosis: 40.79%

The dataset is reasonably balanced and does not require oversampling.

## Correlation Analysis

Strongest correlations with diagnosis:

1. Hormone Level Abnormality
2. Chronic Pain Level
3. Menstrual Irregularity
4. Infertility

Age showed negligible correlation with diagnosis.

## Key Observation

The synthetic dataset exhibits relatively weak correlations overall, indicating limited predictive signal and motivating future integration of richer clinical datasets.

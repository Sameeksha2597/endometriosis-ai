# Endometriosis Patient State Intelligence System

## Project Overview

Endometriosis is a chronic inflammatory condition affecting millions of women worldwide and is characterized by highly variable symptom patterns, menstrual flare-ups, pain episodes, and quality-of-life impacts. Traditional symptom analysis often focuses on individual symptoms in isolation, making it difficult to understand broader patient health trajectories.

This project develops a longitudinal patient analytics framework using real-world symptom tracking data from endometriosis patients. The system combines exploratory data analysis, symptom forecasting, unsupervised patient state discovery, temporal state transition modeling, and machine learning-based state prediction to identify clinically meaningful patient health states and forecast future patient conditions.

---

## Dataset

### Source

KI-Endolist Longitudinal Symptom Tracking Dataset

### Dataset Characteristics

* 34 patients
* 5,112 daily observations
* 387 tracked symptom and health variables
* Longitudinal daily symptom records
* Menstrual cycle information
* Physical and emotional wellbeing indicators
* Gastrointestinal symptom tracking
* Pain severity measurements

---

## Project Objectives

The project was designed to answer three key questions:

### 1. Symptom Intelligence

Which symptoms are most important and how are they related?

### 2. State Discovery

Can clinically meaningful patient states be identified from symptom patterns?

### 3. State Intelligence

Can a patient's future health state be predicted using current symptoms and cycle information?

---

# Phase 1: Symptom Intelligence

## Correlation Analysis

A correlation matrix was constructed using core patient health indicators.

### Strongest Relationships

| Variables                                | Correlation |
| ---------------------------------------- | ----------: |
| Period ↔ Bleeding                        |        0.81 |
| Emotional Condition ↔ Physical Condition |        0.62 |
| Bleeding ↔ Physical Condition            |       -0.28 |

### Key Insights

* Menstrual activity strongly drives bleeding severity.
* Physical and emotional wellbeing are closely connected.
* Increased bleeding is associated with reduced physical wellbeing.

---

## Symptom Forecasting

### Objective

Predict next-day symptom severity using current patient information.

### Baseline Forecasting Model

Target Variable:

* Tomorrow's Lower Back Pain

Performance:

* MAE: 0.662
* MSE: 0.727
* R²: 0.176

---

## Temporal Feature Engineering

To improve forecasting performance, symptom history features were introduced:

* Pain Lag 1
* Pain Lag 2
* Pain Lag 3
* 3-Day Rolling Average

### Improved Forecasting Model

Performance:

* MAE: 0.626
* MSE: 0.608
* R²: 0.358

### Result

Temporal symptom history increased predictive performance by more than 100%, demonstrating that symptom persistence is an important factor in future symptom severity.

---

## Multi-Symptom Forecasting

Five major symptoms were independently modeled.

| Symptom          | Training Rows |    R² |
| ---------------- | ------------: | ----: |
| Abdominal Cramps |           862 | 0.337 |
| Lower Back Pain  |          1087 | 0.316 |
| Period Pain      |           301 | 0.230 |
| Nausea           |           755 | 0.176 |
| Headache         |           705 | 0.121 |

### Findings

* Abdominal cramps and lower back pain were the most predictable symptoms.
* Period pain showed moderate predictability.
* Headache exhibited limited predictive signal.
* Symptom-level forecasting achieved moderate performance overall due to substantial day-to-day variability.

---

# Phase 2: Patient State Discovery

## Patient State Clustering

Instead of analyzing symptoms individually, patients were grouped into latent health states using K-Means clustering.

### Features Used

* Cycle Day
* Period Status
* Bleeding Severity
* Emotional Condition
* Physical Condition
* Stool Characteristics

### Cluster Distribution

| Cluster   | Size |
| --------- | ---: |
| Cluster 0 |  839 |
| Cluster 1 |  305 |
| Cluster 2 |  334 |

---

## Discovered Health States

### Cluster 0 — Stable Days

Characteristics:

* High physical wellbeing (7.15/10)
* High emotional wellbeing (7.15/10)
* Minimal bleeding
* Mostly outside menstruation

Interpretation:

Stable low-symptom health state.

---

### Cluster 1 — Chronic Symptom Burden

Characteristics:

* Low physical wellbeing (4.41/10)
* Low emotional wellbeing (4.57/10)
* Minimal menstrual activity

Interpretation:

Persistent symptom burden independent of menstrual phase.

---

### Cluster 2 — Menstrual Flare State

Characteristics:

* Active menstruation
* Highest bleeding severity
* Reduced physical wellbeing
* Reduced emotional wellbeing

Interpretation:

Cycle-driven flare state.

---

# Phase 3: Patient State Transition Analysis

To understand how patient health evolves over time, a state transition matrix was constructed.

## State Persistence

| Transition                          | Probability |
| ----------------------------------- | ----------: |
| Stable → Stable                     |       87.0% |
| Chronic Symptom Burden → Same State |       70.4% |
| Menstrual Flare → Same State        |       79.4% |

### Findings

* Stable health states are highly persistent.
* Menstrual flare states frequently continue across multiple days.
* Chronic symptom burden states show moderate persistence.
* Direct transitions between Stable Days and Menstrual Flare Days are uncommon (<5%).

### Interpretation

Patient health states exhibit meaningful temporal structure rather than random symptom fluctuations.

---

# Phase 4: Patient State Intelligence

## Objective

Predict a patient's next-day health state.

### Target Classes

* Stable Day
* Chronic Symptom Burden Day
* Menstrual Flare Day

---

## Machine Learning Model

Model:

* Random Forest Classifier

Input Features:

* Cycle Day
* Period Status
* Bleeding Severity
* Physical Condition
* Emotional Condition
* Stool Characteristics
* Current Patient State

---

## Model Performance

### Overall Accuracy

80.95%

### Classification Performance

| State                  | Precision | Recall | F1 Score |
| ---------------------- | --------: | -----: | -------: |
| Stable Day             |      0.86 |   0.87 |     0.86 |
| Chronic Symptom Burden |      0.67 |   0.60 |     0.63 |
| Menstrual Flare Day    |      0.78 |   0.83 |     0.80 |

---

## Feature Importance

| Feature               | Importance |
| --------------------- | ---------: |
| Cycle Day             |      0.259 |
| Current State         |      0.191 |
| Physical Condition    |      0.131 |
| Emotional Condition   |      0.115 |
| Stool Characteristics |      0.108 |
| Bleeding Severity     |      0.100 |
| Period Status         |      0.097 |

### Key Findings

* Cycle position is the strongest driver of future patient state.
* Current health state strongly influences future outcomes.
* Physical and emotional wellbeing provide substantial predictive signal.
* State-level prediction significantly outperformed individual symptom forecasting.

---

# Business and Clinical Impact

This project demonstrates that endometriosis symptom trajectories can be modeled more effectively through patient health states rather than isolated symptom prediction.

Potential applications include:

* Flare-up risk monitoring
* Personalized symptom management
* Digital health tracking platforms
* Clinical decision support systems
* Patient health trajectory forecasting

---

# Technical Stack

### Languages

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

### Machine Learning Techniques

* Correlation Analysis
* Random Forest Regression
* Random Forest Classification
* K-Means Clustering
* Temporal Feature Engineering
* State Transition Modeling

---

# Key Project Outcome

The project successfully transformed raw longitudinal symptom records into a patient state intelligence framework capable of:

1. Discovering clinically interpretable patient health states.
2. Quantifying state transition dynamics.
3. Forecasting future symptom severity.
4. Predicting future patient health states with 80.95% accuracy.

These findings suggest that longitudinal state-based modeling offers a promising approach for understanding and predicting endometriosis symptom trajectories.


## Module 3: Medical Imaging Intelligence (GLENDA / ENID)

### Dataset

- 1022 laparoscopic images
- Endometriosis: 533
- No Endometriosis: 489

### Model

- ResNet50 Transfer Learning
- PyTorch

### Results

- Validation Accuracy: 99.35%
- Test Accuracy: 95.45%
- Precision: 95%
- Recall: 95%
- F1 Score: 95%

### Explainability

Grad-CAM analysis demonstrated that model attention focused on localized tissue regions associated with abnormal pelvic structures, providing interpretable visual explanations for predictions.
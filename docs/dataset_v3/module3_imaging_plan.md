# Module 3: Medical Imaging Intelligence

## Objective

Develop a computer vision system capable of identifying endometriosis from laparoscopic surgical images.

This module extends the project beyond tabular symptom analysis and longitudinal patient modeling by incorporating medical imaging data.

---

## Dataset

### Source

GLENDA / ENID Dataset

### Characteristics

* Total Images: 1022
* Endometriosis: 533
* No Endometriosis: 489
* Resolution: 640 × 360
* RGB Images
* Binary Classification Task

---

## Problem Definition

### Input

Laparoscopic image

### Output

Prediction:

* Endometriosis
* No Endometriosis

---

## Modeling Strategy

### Phase 1: Dataset Exploration

Completed:

* Dataset inspection
* Class distribution analysis
* Image sample visualization
* Dataset documentation

---

### Phase 2: Baseline Image Classification

Planned:

* Train / Validation / Test Split
* Image preprocessing
* Image augmentation
* Baseline transfer learning model

Candidate architectures:

* ResNet50
* EfficientNet-B0

---

### Phase 3: Model Evaluation

Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

Visualizations:

* Confusion Matrix
* ROC Curve

---

### Phase 4: Explainable AI

Goal:

Understand which image regions influence model predictions.

Technique:

* Grad-CAM

Expected Outputs:

* Activation heatmaps
* Model interpretation examples
* Error analysis

---

## Expected Deliverables

### Notebook 07

Dataset Exploration

### Notebook 08

Image Classification

### Documentation

* Dataset Summary
* Modeling Results
* Explainability Findings

---

## Success Criteria

A successful Module 3 implementation should:

* Achieve strong classification performance
* Demonstrate robust generalization
* Provide interpretable predictions
* Show clinically meaningful visual explanations through Grad-CAM

---

## Relationship to Previous Modules

### Module 1

Structured tabular prediction

### Module 2

Longitudinal symptom and patient-state intelligence

### Module 3

Medical imaging intelligence

Together, the three modules provide complementary perspectives on endometriosis prediction and analysis.

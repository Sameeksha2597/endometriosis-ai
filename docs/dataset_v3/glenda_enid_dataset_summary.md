# GLENDA / ENID Dataset Summary

## Dataset Overview

The GLENDA / ENID dataset contains laparoscopic surgical images for endometriosis detection.

### Dataset Statistics

* Total Images: 1022
* Endometriosis Images: 533
* No Endometriosis Images: 489
* Resolution: 640 × 360
* Color Format: RGB

### Class Distribution

The dataset is approximately balanced:

| Class            | Images |
| ---------------- | -----: |
| Endometriosis    |    533 |
| No Endometriosis |    489 |

This reduces the need for aggressive balancing techniques during model training.

## Image Characteristics

The images are laparoscopic views of pelvic anatomy acquired during surgical procedures.

Observed visual patterns include:

* Dark blue-black lesions
* Discolored tissue regions
* Vascular abnormalities
* Anatomical structures associated with endometriosis

## Planned Modeling Approach

The imaging pipeline will focus on binary classification:

* Endometriosis
* No Endometriosis

Planned techniques:

* Transfer Learning
* ResNet50
* EfficientNet-B0
* Data Augmentation
* Explainable AI (Grad-CAM)

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

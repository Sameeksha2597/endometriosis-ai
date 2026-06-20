# GLENDA / ENID Dataset Summary

## Dataset Overview

- Total Images: 1022
- Endometriosis: 533
- No Endometriosis: 489
- Image Resolution: 640 × 360
- Image Format: RGB

## Class Balance

The dataset is approximately balanced, reducing the need for aggressive class-weighting techniques.

## Initial Observations

Images consist of laparoscopic views of pelvic anatomy and visible endometriotic lesions. Lesions appear as dark, blue-black, or discolored regions against surrounding tissue.

## Planned Approach

- Transfer Learning
- ResNet50 / EfficientNet-B0
- Binary Classification
- Endometriosis vs No Endometriosis

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
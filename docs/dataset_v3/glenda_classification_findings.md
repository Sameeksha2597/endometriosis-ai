# GLENDA ENID Classification Findings

## Objective

Develop a computer vision model capable of detecting endometriosis from laparoscopic surgical images.

## Dataset

* Total Images: 1022
* Endometriosis: 533
* No Endometriosis: 489
* Resolution: 640 × 360 RGB

## Model

* Architecture: ResNet50
* Approach: Transfer Learning
* Framework: PyTorch

## Training Performance

| Epoch | Train Accuracy | Validation Accuracy |
| ----- | -------------: | ------------------: |
| 1     |         71.89% |              88.24% |
| 2     |         93.01% |              94.77% |
| 3     |         95.38% |              93.46% |
| 4     |         99.16% |              96.73% |
| 5     |         99.44% |              99.35% |

Best Validation Accuracy: 99.35%

## Test Performance

| Metric    |  Value |
| --------- | -----: |
| Accuracy  | 95.45% |
| Precision |    95% |
| Recall    |    95% |
| F1 Score  |    95% |

## Confusion Matrix

| Actual           | Predicted Endometriosis | Predicted No Endometriosis |
| ---------------- | ----------------------: | -------------------------: |
| Endometriosis    |                      80 |                          3 |
| No Endometriosis |                       4 |                         67 |

Total Misclassifications: 7 / 154

## Key Findings

* The model achieved strong generalization on unseen test data.
* Endometriosis lesions contain highly discriminative visual features.
* Transfer learning proved highly effective despite the relatively small dataset size.
* Performance substantially exceeded symptom forecasting models developed in earlier modules.

## Conclusion

Medical imaging provided the strongest predictive signal among all datasets used in the project. A ResNet50 transfer-learning approach achieved 95.45% test accuracy while maintaining balanced precision and recall across both classes.

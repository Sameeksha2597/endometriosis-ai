# Model Comparison

## Logistic Regression

* Accuracy: 0.635
* ROC-AUC: 0.657

## Random Forest

* Accuracy: 0.598
* ROC-AUC: 0.610

## XGBoost

* Accuracy: 0.631
* ROC-AUC: 0.644

## Observations

Logistic Regression achieved the strongest ROC-AUC score despite being the simplest model.

Random Forest and XGBoost did not outperform the baseline model.

This suggests that feature richness rather than model complexity is the primary limitation of the dataset.

## Explainability

SHAP analysis identified:

1. Hormone Level Abnormality
2. BMI
3. Chronic Pain Level

as the most influential predictors.

## Conclusion

Future improvements should prioritize richer clinical features, imaging data, biomarkers, and longitudinal symptom tracking rather than extensive hyperparameter tuning.

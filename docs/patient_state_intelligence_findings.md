# Patient State Intelligence Findings

## Objective

Predict a patient's next-day health state using current symptom and cycle information.

---

## Model

Random Forest Classifier

---

## Performance

### Overall Accuracy

80.95%

### Classification Metrics

| State | Precision | Recall | F1 Score |
|---------|----------:|--------:|---------:|
| Stable Day | 0.86 | 0.87 | 0.86 |
| Bad Symptom Day | 0.67 | 0.60 | 0.63 |
| Menstrual Flare Day | 0.78 | 0.83 | 0.80 |

---

## Feature Importance

| Feature | Importance |
|----------|-----------:|
| Cycle Day | 0.259 |
| Current State | 0.191 |
| Physical Condition | 0.131 |
| Emotional Condition | 0.115 |
| Stool Type | 0.108 |
| Bleeding | 0.100 |
| Period | 0.097 |

---

## Key Findings

- Cycle day is the strongest predictor of future patient state.
- Current state strongly influences future state.
- Physical and emotional wellbeing contribute substantially to state prediction.
- Stable and menstrual flare states can be predicted reliably.

---

## Conclusion

State-level prediction substantially outperformed individual symptom forecasting. Modeling endometriosis as patient health states appears more effective than predicting isolated symptoms.

## Patient State Intelligence

A Random Forest classifier was trained to predict a patient's next-day health state using cycle information, bleeding severity, physical condition, emotional condition, stool characteristics, and current state.

Results:

* Overall Accuracy: 80.95%
* Stable Day Recall: 87%
* Period Flare Day Recall: 83%
* Bad Symptom Day Recall: 60%

The model demonstrated strong ability to identify stable and menstrual flare states, indicating that patient health trajectories exhibit meaningful temporal structure. State-level prediction substantially outperformed individual symptom forecasting, suggesting that endometriosis symptom patterns may be more predictable when modeled as patient states rather than isolated symptoms.
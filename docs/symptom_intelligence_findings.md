# Symptom Intelligence Findings

## Dataset

- 34 patients
- 5112 daily observations
- 387 symptom variables

## Key Findings

### Correlation Analysis

- Period ↔ Bleeding: 0.81
- Emotional ↔ Physical Condition: 0.62
- Bleeding ↔ Physical Condition: -0.28

### Patient Clustering

- Cluster 0:839
- Cluster 1:334
- Cluster 2:305

## Patient State Clustering

K-Means clustering (k=3) identified three distinct symptom states:

### Cluster 0: Low Symptom Burden
- Good physical condition (7.15/10)
- Good emotional condition (7.15/10)
- Minimal bleeding
- Mostly outside menstrual phase

### Cluster 1: Chronic Symptom Burden
- Poor physical condition (4.41/10)
- Poor emotional condition (4.57/10)
- Low menstrual activity
- Suggests persistent symptom burden independent of menstruation

### Cluster 2: Menstrual Flare State
- Active menstruation
- Highest bleeding scores
- Reduced physical and emotional wellbeing

## Future Work

- Symptom forecasting
- Flare-up prediction
- Personalized recommendations

Patient state transitions revealed strong persistence.

Cluster 0 (Stable Days) remained stable 87.0% of the time.

Cluster 1 (Bad Symptom Days) persisted 70.4% of the time.

Cluster 2 (Period Flare Days) persisted 79.4% of the time.

Direct transitions between Stable Days and Period Flare Days were rare (<5%), suggesting that the discovered states represent meaningful physiological conditions rather than random clustering artifacts.
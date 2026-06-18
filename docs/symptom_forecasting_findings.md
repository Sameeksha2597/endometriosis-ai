Target:
Tomorrow's Lower Back Pain

Forecasting V1:
MAE: 0.662
MSE: 0.727
R²: 0.176

Forecasting V2 (Lag Features):
MAE: 0.626
MSE: 0.608
R²: 0.358

Improvement:
R² increased by more than 100%.

Key Insight:
Pain history and cycle position are the strongest predictors of future symptom severity.

## Multi-Symptom Forecasting (V2)

| Symptom | Rows | R² |
|----------|------:|------:|
| Abdominal cramps | 862 | 0.337 |
| Lower back pain | 1087 | 0.316 |
| Period pain | 301 | 0.230 |
| Nausea | 755 | 0.176 |
| Headache | 705 | 0.121 |

Key observations:
- Abdominal cramps and lower back pain are the most forecastable symptoms.
- Period pain shows moderate temporal predictability.
- Headache is difficult to predict using cycle and symptom-history features alone.
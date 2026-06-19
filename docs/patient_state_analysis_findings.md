

# Patient State Analysis Findings

## Patient State Clustering

K-Means clustering (k=3) identified three distinct symptom states.

### Cluster 0: Stable Days

- Good physical condition (7.15/10)
- Good emotional condition (7.15/10)
- Minimal bleeding
- Mostly outside menstrual phase

Size: 839 observations

---

### Cluster 1: Chronic Symptom Burden

- Poor physical condition (4.41/10)
- Poor emotional condition (4.57/10)
- Low menstrual activity
- Persistent symptom burden independent of menstruation

Size: 305 observations

---

### Cluster 2: Menstrual Flare State

- Active menstruation
- Highest bleeding scores
- Reduced physical and emotional wellbeing

Size: 334 observations

---

## State Transition Analysis

Patient state transitions revealed strong persistence.

| Transition | Probability |
|------------|------------:|
| Stable → Stable | 87.0% |
| Bad Symptom Day → Bad Symptom Day | 70.4% |
| Menstrual Flare → Menstrual Flare | 79.4% |

### Key Findings

- Stable days are highly persistent.
- Menstrual flare states often continue across multiple days.
- Bad symptom days show moderate persistence.
- Direct transitions between Stable Days and Menstrual Flare Days are rare (<5%).

### Conclusion

The discovered states exhibit meaningful temporal structure and represent clinically interpretable patient conditions rather than random clusters.

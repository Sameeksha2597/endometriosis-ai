# Endometriosis AI — Research Matrix

Primary literature base: 9 uploaded papers. Extraction is strictly source-grounded. "Not Reported" = field absent in paper. Three uploads are reviews (no primary dataset), one is a study protocol (no results yet), one is a correction notice, and one is tangential (intrauterine adhesion, not endometriosis) but retained for imaging-pipeline value.

## Research Matrix

| Paper ID | Paper Title | Authors | Year | Journal / Conference | Research Objective | Dataset Source | Dataset Type | Sample Size | Population | Data Modality | Feature Categories | Key Features | Target Variable | ML Models Used | Best Model | Evaluation Metrics | Best Results | Explainability Method | External Validation | Clinical Utility | Key Limitations | Research Gap Identified | Reusable Ideas for My Project | Portfolio Relevance (1-10) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P001 | Artificial Intelligence in the Management of Women with Endometriosis and Adenomyosis: Can Machines Ever Be Worse Than Humans? | Cetera, Tozzi, Chiappa, Castiglioni, Merli, Vercellini | 2024 | J. Clin. Med. (MDPI) | Narrative review of AI roles across endometriosis/adenomyosis diagnosis, imaging, treatment, surgery, admin, research | Literature (PubMed, searched 11 Dec 2023) | Not Reported (review) | Not Reported | Women with endometriosis/adenomyosis (literature-level) | Clinical, Imaging (US/MRI), Symptoms, Biomarkers, Omics (as surveyed) | Clinical, Imaging Features, Biomarkers, Genomic Markers | Age, symptoms, comorbidities, US/MRI findings, CA125, omics (surveyed, not modeled) | Endometriosis diagnosis / prediction / management (survey scope) | LLMs (ChatGPT, Med-PaLM 2), DL, ML (surveyed, not trained here) | Not Reported (no model trained) | Not Reported (cites others: e.g. 90% AUC US pilot, 92% surgical) | Not Reported (synthesizes others' results) | None | Not Reported | Frames where a decision-support tool fits clinical workflow: diagnosis, drug-interaction alerts, risk stratification, admin | No original data; narrative, not systematic; selection bias | Lack of prospective/RCT validation; no head-to-head vs existing decision algorithms; interpretability of DL | Use as scoping map of use-cases + WHO 6-point governance frame for Responsible-AI layer | 6 |
| P002 | Machine learning algorithms as new screening approach for patients with endometriosis | Bendifallah, Puchar, Suisse, Delbos, Poilblanc, Descamps, Golfier, Touboul, Dabi, Daraï | 2022 | Scientific Reports (Nature) | Train + externally validate MLA to predict endometriosis likelihood from clinical/symptom features | Ziwig Health platform (train); ENDOmiARN NCT04728152 (validation) | Questionnaire / Clinical Dataset | Train 1126 endo + 608 controls (filtered from 8000); Validation 100 | Women of childbearing age, France; surgical diagnosis in both sets | Symptoms, Clinical | Demographics, Medical History, Symptoms, Phenotype, Treatment | 16 selected features: age, BMI, dysmenorrhea/VAS, abdominal pain, family history, period length, etc. | Endometriosis diagnosis (binary) | LR, Decision Tree, Random Forest, XGBoost, Voting (soft/hard); Chi-square feature selection | RF / XGBoost / Soft Voting (comparable top) | Sensitivity, Specificity, F1, AUC | Validation: XGB AUC 0.93, RF AUC 0.92; sens up to 0.95, spec up to 0.92 | None (correlation matrix + chi-square only) | Yes (ENDOmiARN prospective cohort) | Patient-facing/GP symptom questionnaire to triage before laparoscopy; supports shared decision-making | Self-report label bias; ~20% endo asymptomatic; small validation n (100); no discordant cases | Lack of multimodal fusion; no model interpretability; questionnaire-only | Symptom-questionnaire screening pipeline; 16-feature baseline; XGB/RF + soft-voting ensemble; external-validation discipline | 10 |
| P003 | FEMaLe: The use of machine learning for early diagnosis of endometriosis based on patient self-reported data — Study protocol of a multicenter trial | Balogh, Hudelist, Blizņuks, Raghothama, Becker, Horace, et al. | 2024 | PLoS ONE | Protocol to build self-report big-data repository (Lucy app) + ML for early diagnosis | Lucy app (planned); EU Horizon 2020 FEMaLe project | Questionnaire / EHR (planned, longitudinal) | Planned: 5,000 endo + 5,000 controls; repository cited >1M records | Women, multicenter; 1-yr follow-up | Symptoms, Clinical, Lifestyle (longitudinal self-report) | Demographics, Symptoms, Mental/Physical Health, Economic, Nutrition, Lifestyle | Baseline + longitudinal questionnaire items, VAS, EQ-5D-5L, CSI-9, EHP-5 | Endometriosis diagnosis from self-reported data | Planned: Random Forest, LSTM, Transformer; DBSCAN + UMAP (clustering/dim-reduction); Cramér's V | Not Reported (protocol; no results) | Planned: sensitivity, specificity (post-completion) | Not Reported (no datasets generated yet) | Longitudinal app-based early-detection screening reducing diagnostic delay | No data yet; protocol only; 1:1 case-control may not reflect prevalence | Lack of deployed longitudinal/time-series models; real-world validation pending | Longitudinal symptom-tracking design; LSTM for temporal symptom progression; UMAP/DBSCAN patient segmentation; app architecture | 8 |
| P004 | Investigating the role of AI in the diagnosis and prediction of endometriosis using ultrasound images: a systematic review | Not Reported (multi-author) | 2025 | Reprod. Health (s12978-025-02245-1) | PRISMA systematic review of AI on US images for endometriosis | PubMed, Web of Science, Scopus | Not Reported (review of 5 studies) | 5 included studies | Women, US-imaged (study-level) | Ultrasound, Imaging | Imaging Features, Radiomics | US image features (study-dependent) | Endometriosis diagnosis / prediction (imaging) | ML + DL incl. CNN (across 5 studies) | DL (CNN) reported highest | Accuracy, AUC, Sensitivity, Specificity | DL acc 0.89–0.93, AUC ~0.90; ML acc 0.80–0.85, AUC 0.75–0.80; sens 0.78–0.92, spec 0.74–0.89 | Notes ML > DL on interpretability (qualitative) | Not Reported (review) | US-based AI screening adjunct to transvaginal scan; earlier triage | Only 5 studies; fragmented, inconsistent; heterogeneity; generalizability | Lack of real-world validation; clinician/patient awareness gap | Benchmarks for US-imaging models (target AUC ~0.90); ML-vs-DL interpretability tradeoff | 7 |
| P005 | Identification and validation of a novel machine learning model for predicting severe pelvic endometriosis: A retrospective study | Not Reported (China Medical University group) | 2025 | Scientific Reports (s41598-025-96093-5) | Develop interpretable ML model to predict severe (rASRM IV) endometriosis pre-surgery | First Hospital of China Medical University | Clinical + Ultrasound Dataset | 308 analyzed (from 471); train 246 / test 62 (8:2) | Endo patients >18, surgically + pathology confirmed; single-center, China | Clinical, Ultrasound, Laboratory | Demographics, Symptoms, Menstrual History, Lab Markers, Imaging | From 39 vars → LASSO 18 → final 6: negative sliding sign, PFOC, bilateral OEs, severe dysmenorrhea, eosinophil%, MCRS; CA125, VAS | Severe endometriosis (binary, rASRM stage IV) | LR, rpart, RF, XGBoost, SVM, KNN, NNET; LASSO feature selection; 10-fold CV + grid search | Random Forest (6-feature final) | AUROC, Accuracy | Full RF AUC 0.744; final 6-feature RF AUROC 0.865 train / 0.720 test | SHAP (global + local) | No (single-center, internal test split only) | Pre-operative risk stratification of severe disease to plan surgery/referral | Single-center; modest n (308); no external validation; class context | Lack of external/prospective validation; stage prediction under-explored | LASSO→RF pipeline; SHAP global+local layer; staging (not just diagnosis) as target; RF imputation for missing data | 9 |
| P006 | Empowering women through intelligent care: a narrative review of AI-driven digital innovations for endometriosis diagnosis, education, and equity | Not Reported (multi-author) | 2025 | (s44326-025-00061-2) | Narrative review of AI/FemTech for diagnosis, education, equity + barriers | Literature + FemTech platform survey | Not Reported (review) | Not Reported | Women with endometriosis; FemTech users | Symptoms, Imaging, Multimodal (surveyed) | Symptoms, Imaging Features, Clinical Notes | Symptom-tracking, imaging, decision-support inputs (surveyed) | Endometriosis diagnosis / education / equity (survey) | ML, DL/CNN, NLP (surveyed) | Not Reported | Not Reported | Not Reported (qualitative barriers focus) | Discusses opacity/accountability as a barrier (no method) | Not Reported | Symptom-tracking apps + decision support; equity-aware deployment design | Small/biased datasets; EHR interoperability; bias; digital divide; stigma | Lack of condition-specific algos; lack of real-world validation; ethical design gaps | Equity + ethical-AI design checklist; multimodal (clinical+imaging+symptom+genomic) data-integration argument; bias-audit layer | 6 |
| P007 | Clinical use of artificial intelligence in endometriosis: a scoping review | Sivajohan et al. | 2022 | npj Digital Medicine (s41746-022-00638-1) | Scoping review of AI applications across endometriosis (pathology, diagnostics, prediction, management) | PubMed + databases | Not Reported (review of 79 papers) | 1309 titles → 79 papers; avg sample 245, range from 26 | Endometriosis patients (study-level) | Clinical, Imaging, Genomics/Transcriptomics, Symptoms, Multimodal | Clinical factors, Transcriptomics, Imaging, Symptoms | Clinical factors (n=6 studies), transcriptomics (n=5), others | Diagnosis (47.2%), prediction (44.4%), management of endometriosis | LR, RF, DT, SVM, KNN, Naive Bayes, NN, Voting, DL, ensembles | ML most common; then DT, RF, SVM | Sensitivity, Specificity | Surveyed models generally sens/spec >85% | Notes interpretability limits across field | Not Reported (mostly retrospective; 16 prospective; 0 RCT) | Field-level map of where AI is applied + maturity | Predominantly retrospective; small samples; no RCTs; heterogeneity | Lack of prospective/RCT; lack of standardization; deployment gap | Master taxonomy of models × tasks; benchmark of sample sizes; justifies multimodal + prospective design | 9 |
| P008 | Deep Learning-Based Three-dimensional Transvaginal Ultrasound in Diagnosis of Intrauterine Adhesion | Li et al. | 2021 | Scientific Programming (Hindawi) | DL image enhancement (PDE) + HSegNet CNN segmentation for 3D TVUS diagnosis (intrauterine adhesion, NOT endometriosis) | Single hospital | Ultrasound / Imaging Dataset | 75 patients | Suspected intrauterine adhesion, 24–45 yrs, single-center | Ultrasound (3D TVUS), Imaging | Imaging Features (segmentation), Quantitative (V, VI, FI, VFI) | Endometrial volume + blood-flow params; segmented adhesion regions | Intrauterine adhesion diagnosis + grading | PDE/TV denoising + HSegNet (CNN, encoder + auto-context) | HSegNet CNN | Accuracy, Sensitivity, Specificity (vs hysteroscopy) | Auto-label acc 97.3%; diagnostic acc 97.14%, sens 96.6%, spec 72% | None | No (single-center; vs hysteroscopy gold standard) | Automated US image labeling/segmentation to support non-invasive diagnosis | Small n (75); single-center; misses mild/peripheral adhesions; low spec (72%) | Lack of generalizability; not endometriosis-specific | Image preprocessing (denoise/enhance) + CNN segmentation pipeline; quantitative imaging features for grading | 5 |
| P009 | Correction: Diagnostic accuracy of machine learning for endometriosis: a systematic review and meta-analysis | Zhang, Lv, Li, Zhang, Ru, Ma | 2026 | Frontiers in Endocrinology | Correction notice (reference-list fixes) to a systematic review & meta-analysis of ML diagnostic accuracy | Parent: systematic review/meta-analysis | Not Reported (correction) | Not Reported (parent: meta-analysis of multiple studies) | Endometriosis (parent meta-analysis) | Clinical, Imaging, Biomarkers (parent scope) | Not Reported | Not Reported | ML diagnostic accuracy for endometriosis (parent) | Not Reported (correction); parent surveys ML/DL | Not Reported | Pooled sensitivity/specificity (parent — not in this correction) | Not Reported in correction | Not Reported | Not Reported | Pooled accuracy benchmark exists in parent paper (fetch full meta-analysis) | This file is only a reference correction; no extractable data | N/A — retrieve the parent meta-analysis for pooled estimates | Use parent meta-analysis (doi 10.3389/fendo.2025.1735567) for pooled sens/spec benchmark | 4 |

---

## Section 1: Cross-Paper Analysis

**Most Common Dataset Types.** Questionnaire/clinical (P002, P003, P005) and ultrasound imaging (P004, P005, P008) dominate among primary-data papers. Reviews (P001, P006, P007, P009) report no own dataset.

**Most Common Feature Categories.** Symptoms + demographics + medical history (clinical/questionnaire track) and imaging/radiomics features (ultrasound track). CA125 and dysmenorrhea/VAS recur across both tracks.

**Most Common Target Variables.** Binary endometriosis diagnosis (P002, P003, P004) is most frequent. Severe/stage-IV endometriosis (P005) is the notable stratification target. P008 targets a different condition (intrauterine adhesion).

**Most Common Models.** Random Forest and XGBoost appear in every primary structured-data study (P002, P005) and across the review taxonomies (P001, P007). CNN dominates the imaging track (P004, P008). LR and SVM are standard baselines.

**Most Common Evaluation Metrics.** Sensitivity, Specificity, AUC/AUROC, Accuracy, F1. AUC is the shared comparison currency.

---

## Section 2: Model Frequency Analysis

| Model | Number of Papers | Best Use Case |
|---|---|---|
| Random Forest | P002, P005, P007 (+ planned P003) | Strong tabular baseline; top performer in both primary structured-data studies |
| XGBoost | P002, P005, P007 | Best/near-best AUC on symptom + clinical/imaging tabular features |
| Logistic Regression | P002, P005, P007 | Interpretable baseline; weak alone on imbalanced data (P002 LR collapsed) |
| Decision Tree / rpart | P002, P005, P007 | Simple, interpretable; component of ensembles |
| SVM | P005, P007 | Mid-tier tabular baseline |
| KNN | P005, P007 | Baseline only |
| Naive Bayes | P007 | Lightweight baseline (survey) |
| Voting / Ensemble | P002, P007 | Soft voting matched RF/XGB top tier in P002 |
| Neural Net (NNET/MLP) | P005, P007 | Tabular baseline; no standout |
| CNN (incl. HSegNet) | P004, P008 (+P006 survey) | Ultrasound image classification/segmentation; highest imaging accuracy |
| LSTM | P003 (planned) | Longitudinal symptom time-series |
| Transformer | P003 (planned) | Large self-report pattern recognition |
| LLM (ChatGPT, Med-PaLM 2) | P001 (survey) | Knowledge access, differential-diagnosis support |

---

## Section 3: Feature Frequency Analysis

| Feature | Frequency Across Papers | Clinical Importance |
|---|---|---|
| Dysmenorrhea / VAS pain | P002, P005 (+reviews) | Core symptom; high discriminative weight |
| Age | P002, P005 (+P001 cancer-risk) | Standard demographic predictor |
| CA125 | P005 (+P001 survey) | Established but limited biomarker |
| Family history of endometriosis | P002 | Genetic-risk signal |
| Negative sliding sign (US) | P005 | Top SHAP feature for severe disease |
| Bilateral OEs / OE morphology (US) | P005 | Imaging marker of severity |
| PFOC (pelvic fluid cul-de-sac) | P005 | Imaging severity marker |
| Abdominal/pelvic pain outside menses | P002 | Strong symptom discriminator |
| BMI | P002 | Common covariate (weak) |
| Imaging/radiomics features | P004, P008 | Backbone of DL imaging models |
| Transcriptomics/omics | P007 (n=5 studies surveyed) | High-signal but costly, low deployability |
| Lifestyle / QoL (EQ-5D, EHP) | P003 (planned) | Longitudinal/self-report enrichment |

---

## Section 4: Explainability Analysis

Explainability is the field's weakest layer. Of the primary-data studies, only **P005 uses formal explainability (SHAP, global + local)**. P002 used a correlation matrix and chi-square for feature selection (interpretation, not post-hoc explanation). P004 notes ML's interpretability edge over DL only qualitatively. P006 flags model opacity as a barrier without a method. P008 (segmentation) and P003 (protocol) report none.

Methods observed: **SHAP (1 paper, P005)**; feature-importance / correlation / chi-square / LASSO (P002, P005); attention or LIME — **none**. Major gap: no LIME, no attention-map interpretability on the imaging track, and no patient-facing explanation layer anywhere. SHAP on tabular clinical+US features (P005 pattern) is the proven template to build on.

---

## Section 5: Research Gap Analysis — Top 10

Ranked by composite of clinical impact, novelty, and implementation feasibility.

1. **No multimodal fusion** of symptoms + clinical + labs + imaging in one model (each study stays single-track; P006/P007 explicitly call for it). High impact, high novelty, medium feasibility.
2. **Weak explainability** beyond a single SHAP study — no LIME, no imaging attention, no patient-facing rationale. High impact, high feasibility.
3. **No external/prospective validation** for most structured-data models (P005 single-center; P002 is the rare external-validation exemplar). High impact, medium feasibility.
4. **Stage/severity prediction under-explored** vs binary diagnosis (only P005). High clinical impact, high novelty.
5. **No deployment/MLOps studies** — monitoring, drift, retraining absent across all. High novelty, medium feasibility.
6. **Small, single-center, biased datasets** limit generalizability (P004, P006, P007, P008). High impact, low feasibility (data-bound).
7. **No longitudinal/time-series modeling** of symptom progression yet realized (P003 only planned). Medium-high impact, medium feasibility.
8. **Class imbalance + label noise** from self-report (P002's ~20% asymptomatic caveat) under-addressed. Medium impact, high feasibility.
9. **No head-to-head vs existing clinical decision tools** (P001 flags this). Medium impact, high feasibility.
10. **Equity / bias auditing** largely absent operationally (P006 conceptual only). Medium impact, high feasibility.

---

## Section 6: Architecture Recommendations

### MVP Architecture (grounded in P002 + P005)
- **Data modality:** Symptom questionnaire + basic clinical/demographic (tabular). Optional CA125 if available.
- **Features:** Start from P002's 16-feature symptom set; add P005's severity-relevant clinical items where collectable. LASSO/chi-square selection.
- **Models:** XGBoost and Random Forest as primary; LR as interpretable baseline; soft-voting ensemble (P002 showed parity with top single models).
- **Explainability:** SHAP global + local on the winning tree model (direct P005 transplant).
- **Validation:** Stratified split + 10-fold CV; reserve an external/held-out source from the start (P002 discipline).
- **Target:** Binary endometriosis likelihood (MVP), with a severe-disease head as stretch.

### Advanced Architecture
- **Multimodal learning:** Late/intermediate fusion of (a) tabular symptom+clinical+lab branch (XGB/RF or tabular transformer) with (b) ultrasound imaging branch (CNN, P004/P008 pattern), optionally (c) omics branch (P007, gated by cost/availability).
- **Imaging:** CNN classifier + segmentation (HSegNet-style, P008) with PDE/denoise preprocessing; radiomics feature extraction.
- **Biomarkers:** CA125 and emerging miRNA panels as a structured branch (caveats from P002/P007).
- **Clinical/longitudinal:** LSTM/Transformer over time-series self-report (P003 design) for early-warning trajectory.
- **Explainability:** SHAP for tabular branch + attention/Grad-CAM for imaging branch + unified patient-facing rationale (fills gap #2).
- **Deployment considerations:** MLOps with monitoring, drift detection, scheduled retraining, EHR interoperability, and an equity/bias audit gate (fills gaps #5, #10) — none demonstrated in the corpus, so this is the differentiating contribution.

---

## Section 7: Final Recommendation

1. **Which dataset type to start with:** Symptom/questionnaire + clinical tabular data. It is the most reproducible, lowest-cost, externally-validated track in the corpus (P002) and avoids imaging-acquisition barriers.
2. **Which baseline model to build first:** XGBoost (with RF and an LR baseline), the consistent top tabular performer across P002, P005, P007.
3. **Which explainability method first:** SHAP (global + local), the only formally validated explainability approach in the primary studies (P005) and directly transferable to tabular models.
4. **Most useful paper for MVP development:** **P002 (Bendifallah 2022)** — concrete 16-feature symptom set, full model lineup, and external validation make it a near-drop-in MVP blueprint. **P005** is the close second for the SHAP layer.
5. **Most useful paper for publication-quality extensions:** **P007 (Sivajohan 2022, npj Digital Medicine)** for field-level positioning and gap framing, paired with **P005** as the methodological template (LASSO→RF→SHAP) to extend into the unfilled multimodal + deployment + equity space.

> Note: P009 is only a reference-list correction. For pooled sensitivity/specificity benchmarks, retrieve the parent meta-analysis (Zhang et al., Front. Endocrinol. 2025, doi 10.3389/fendo.2025.1735567), which is not among the uploaded files.

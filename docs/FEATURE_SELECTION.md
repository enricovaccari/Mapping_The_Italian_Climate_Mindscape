# Stakeholder Engagement Plan
*Mapping the Italian Climate Mindscape*  

---


This document records the **feature selection process and findings** for clustering analysis.  
The focus is on combining **quantitative evidence** with **domain knowledge** to ensure interpretability.

---

## 1. Initial Feature Pool
- Source: `03_eda_preprocessing.ipynb`
- Dataset shape: (1008, 12) features
- Categories:
  1. **Demographics** – handled separately in descriptive analysis (not included in clustering).
  2. **Attitudes** – climate concern, global solidarity, environmental concerns, adaptation engagement.
  3. **Experiences** – climate events, heat/flood experience, perceived consequences.
  4. **Preparedness** – domestic responsibility, personal preparedness score.

---

## 2. Feature Scaling Strategy
- All features are **Likert-style items or composite indices** (bounded, no true outliers, skewed distributions).
- **MinMax scaling** was chosen because:
  1. It places all features on the same [0,1] interval.  
  2. It preserves original shapes, important for interpretability.  
  3. It’s easy to explain to non-technical audiences.  

Alternative scalers (StandardScaler, RobustScaler) were considered less suitable given bounded, non-normal distributions.

---

## 3. Variance Analysis
- **Threshold**: 0.02  
- **Result**: 12/12 features retained (none below the threshold).  
- **Observed variance range after scaling**:  
  - Lowest: `climate_event_count` = 0.049  
  - Highest: `infra_consequences` = 0.159  
- **Decision**: No features dropped.

---

## 4. Correlation Analysis
- **Threshold**: |r| > 0.85  
- **Result**: No features exceeded this threshold.  
- **Decision**: No features dropped for redundancy.  
- **Note**: Some moderate correlations (≈0.65–0.7) observed, but retained for interpretability.

---

## 5. Outlier Analysis
- Methods applied on scaled data:  
  1. **IQR** (after Yeo–Johnson transform): 333/1008 flagged (~33%).  
  2. **MAD**: 631/1008 flagged (~63%).  
  3. **Isolation Forest**: 51/1008 flagged (~5%).  

- **Interpretation**:  
  - IQR and MAD inflate outliers because Likert data are skewed but bounded → tails are *real patterns*, not anomalies.  
  - Isolation Forest gives a more realistic estimate (~5%) by detecting rare *combinations* of values.  

- **Decision**: Keep both full dataset and Isolation Forest–filtered version (n=957) for comparative clustering.

---

## 6. Dimensionality Reduction (PCA)

### With Outliers
- 2 PCs explained **37.2%** of variance.  
- 9 PCs explained **95%** of variance.  
- PC1 loaded on **climate concern + engagement**, PC2 on **demographics/experience**.

### Without Outliers
- 2 PCs explained **49.4%** of variance.  
- 8 PCs explained **93.1%** of variance.  
- PC1 again reflected **concern/engagement axis**, PC2 more on **experience consequences**.

**Decision:**  
- PCA used as a **diagnostic/visualization tool**, not as clustering input.  
- Rationale: interpretability is critical for sustainability insights, so clustering relies on raw domain-grounded features.

---

## 7. Feature Engineering
- Composite indices created:  
  1. **Adaptation Engagement Score** – aggregated behavioral/attitudinal items.  
  2. **Preparedness Index** – merged domestic responsibility + personal preparedness.  

- **Benefit**: reduced noise, improved construct validity, alignment with sustainability constructs.

---

## 8. Impact on Clustering Interpretability
1. Removing no features (variance/correlation) ensured completeness but required PCA validation.  
2. Outlier handling (Isolation Forest) provided a cleaner dataset, improving stability.  
3. Domain composites made clusters easier to explain (e.g., “high concern, low preparedness”).  
4. PCA confirmed that latent dimensions exist but supported the decision to prioritize original interpretable variables.

---

## 9. Future Refinement
- Validate with domain experts (sustainability, climate psychology).  
- Compare cluster outcomes with/without Isolation Forest outliers.  
- If interpretability becomes secondary to performance, consider using PCA/factor analysis as clustering input.

---

**Final Note:**  
The final feature set balances **rigor and interpretability**, ensuring clustering outputs are robust, transparent, and meaningful for sustainability-oriented stakeholders.

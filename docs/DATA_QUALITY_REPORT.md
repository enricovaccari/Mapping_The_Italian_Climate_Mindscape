# Stakeholder Engagement Plan
*Mapping the Italian Climate Mindscape*  

---

## 1. Objective
This report documents the data quality assessment process conducted before clustering.  
The goal is to ensure data integrity, transparency, and stakeholder trust by:  
- Identifying potential risks in survey responses.  
- Quantifying data quality issues through metrics.  
- Describing expert validation inputs.  
- Outlining improvement strategies.  

---

## 2. Data Sources
- **Survey dataset** collected from respondents (Likert-style scales, categorical demographics, and composite indices).  
- Two feature groups were distinguished:
  - **Clustering features**: Likert-style responses and composite indices used directly in clustering.  
  - **Descriptive features**: demographic and contextual variables, used to profile and interpret clusters.  

---

## 3. Quality Metrics and Checks

### 3.1 Structural Quality
- **Duplicate rows**: Checked and none retained.  
- **Invalid values**: All features adhered to expected ranges (e.g., Likert 1–5, indices bounded by construction).  
- **Missing values**: Minimal; no systemic missingness. Dropped/respondent-level imputation not required.  

### 3.2 Distributional Checks
- **Skewness**: Many clustering features were right-skewed.  
  - Addressed using **Yeo-Johnson transformation**.  
- **Feature scaling**: Applied **StandardScaler** to stabilize variance (~1 across features).  
- **Low variance features**: Removed only constants (`VarianceThreshold(threshold=0.0)`).  

### 3.3 Outlier Assessment
- Multiple detection methods applied to survey responses:  
  - **IQR**: 376/1008 flagged.  
  - **MAD**: 631/1008 flagged.  
  - **Isolation Forest**: 49/1008 flagged (selected for final filtering).  
- Rationale: IQR and MAD were too aggressive given bounded Likert data; Isolation Forest offered a more balanced identification of anomalous multivariate patterns.  
- **Impact**: Removing 49 outliers reduced distortion in PCA space and improved stability of clustering.  

### 3.4 Multicollinearity
- **Correlation matrices** inspected.  
- No features exceeded redundancy thresholds; some correlated features retained deliberately to preserve distinct conceptual constructs (e.g., climate concern vs adaptation engagement).  

### 3.5 Principal Component Analysis (PCA) Diagnostics
- **2D PCA for visualization**:  
  - PC1 ≈ 26.8%, PC2 ≈ 12.5%, total ≈ 39.3%.  
  - Outliers clearly isolated in PCA space.  
- **PCA for dimensionality reduction**:  
  - With outliers: more components required to reach 90% cumulative variance.  
  - Without outliers: fewer components sufficient → evidence that outliers introduced noise.  
- **Scree plots** confirmed elbow effect and validated 90% threshold as practical cutoff.  

---

## 4. Expert Validation Inputs
- **Survey methodology experts** advised:
  - Not to drop rare demographic categories despite low variance — small groups may hold important insights.  
  - Outlier removal should be conservative, focusing on extreme multivariate anomalies rather than bounded survey extremes.  
- **Data science validation**:
  - Confirmed StandardScaler appropriate for clustering.  
  - Recommended Yeo-Johnson over log transformation (handles zeros/negatives).  

---

## 5. Identified Limitations
- **Low explained variance in 2D PCA** (~39%): makes visual separation fuzzy. Interpretation requires caution.  
- **Survey response bias**: inherent in self-reported data. Cannot be fully eliminated.  
- **Rare categories**: retained for interpretability, but may contribute noise in distance-based clustering.  
- **Bounded Likert data**: classic outlier rules (IQR/MAD) overestimate anomalies since extremes are valid choices.  

---

## 6. Improvement Strategies
- **Future survey design**:
  - Include validation items or attention checks to reduce noise.  
  - Balance categorical options to avoid ultra-rare categories.  
- **Advanced preprocessing**:
  - Explore **Factor Analysis / Multiple Correspondence Analysis (MCA)** for dimensionality reduction better suited to survey data.  
  - Compare clustering stability with and without rare categories.  
- **Monitoring**:
  - Track outlier patterns as new waves of data are collected.  
  - Re-evaluate variance thresholds if data distribution shifts.  

---

## 7. Capstone Connection
This data quality report is integral to the capstone project, as it:  
- **Builds stakeholder confidence** by showing systematic quality checks.  
- **Enables transparent interpretation** of clusters, clarifying how preprocessing choices affect results.  
- **Links technical rigor to interpretability**, ensuring clusters are meaningful in the context of youth climate awareness.  

---

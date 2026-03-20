# Project Charter  
*Mapping the Italian Climate Mindscape*  

---

## 1. Purpose & Scope
This project explores climate awareness in Italy using unsupervised machine learning. The core purpose is to uncover distinct population groups based on their attitudes, beliefs, and levels of concern regarding climate change.  
- **In scope**: Survey data analysis (EIB Climate Survey 2024), preprocessing of Likert-scale responses, and application of clustering methods.  
- **Out of scope**: Policy implementation, causal inference, and supervised prediction (though these may be considered in later extensions).  

---

## 2. Stakeholders
- **Primary**: Policymakers, NGOs, educators, and communication strategists aiming to bridge the gap between climate concern and action.  
- **Secondary**: Academic audiences interested in survey-based clustering methodologies and applied sustainability analytics.  

---

## 3. Objectives
- **Research Objective**: Segment Italian citizens into distinct awareness profiles that reflect differences in climate concern, perception, and action.  
- **Practical Objective**: Provide insights that enable stakeholders to design targeted and inclusive outreach strategies.  
- **Learning Objective**: Demonstrate advanced clustering techniques and critical evaluation as part of a master’s-level data science project.  

---

## 4. Methodology
- **Data Source**: EIB Climate Survey (2024), Italy subset.  
- **Data Type**: Likert-scale survey responses (ordinal variables).  

### Clustering Families Considered
- **Partitional** (e.g., K-Means, K-Medoids)  
  Efficient, interpretable, well-suited for large datasets. Assumes spherical, similarly sized clusters.  
- **Hierarchical** (e.g., Agglomerative with Ward’s linkage)  
  Useful for exploring nested relationships. Doesn’t require *k* upfront but computationally heavier.  
- **Density-Based** (e.g., DBSCAN)  
  Could reveal irregularly shaped awareness clusters and identify outlier groups (e.g., extreme skeptics). Sensitive to parameter tuning.  
- **Model-Based** (e.g., Gaussian Mixture Models)  
  Allows soft cluster assignments, capturing overlapping groups (e.g., citizens partly concerned but partly disengaged). Offers probabilistic insights but computationally heavier.  

### Evaluation
- Internal metrics: Silhouette scores, Davies–Bouldin index.  
- External checks: Interpretability of clusters, alignment with socio-demographic traits.  
- Practical lens: Relevance and usability for stakeholders.  

---

## 5. Impact Pathway
- **Problem**: Italy shows high reported concern for climate change, but limited behavioral follow-through.  
- **Insight Goal**: Make hidden audience segments visible and structured.  
- **Actionability**:  
  - Identify groups (e.g., concerned but passive, skeptical/disengaged, active advocates).  
  - Suggest tailored communication or engagement strategies for each.  
  - Provide probabilistic assignments (via GMM) that reflect nuance where individuals fit across multiple profiles.  

---

## 6. Timeline & Deliverables
- **Milestone 1**: Problem framing & charter draft (✔).  
- **Milestone 2**: Data preprocessing & exploratory analysis.  
- **Milestone 3**: Clustering implementation across selected algorithms.  
- **Milestone 4**: Evaluation, interpretation, and visualization of clusters.  
- **Milestone 5**: Documentation & final report with stakeholder-oriented recommendations.  

---

## 7. Success Metrics
- Identification of stable, interpretable clusters (4–6 meaningful profiles).  
- Evidence that clusters align with relevant socio-demographic or perceptual variables.  
- Demonstration of added value from advanced methods (e.g., DBSCAN for outlier groups, GMM for overlapping profiles).  
- Potential pathways for stakeholders to use results (communication, education, policy design).  
- Timely delivery aligned with master’s capstone deadlines.  

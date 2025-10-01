# Data-Method Alignment
*Mapping the Italian Climate Mindscape*  

---

## 💡 Concept
This dataset is based on the 2024 EIB Climate Survey (Italy), reduced from 150+ Likert-style questions to **20 aggregated features** plus key demographics. The data is mostly ordinal (Likert), with some categorical variables (age, gender, political preference). Applying the data-method alignment framework means connecting these characteristics directly to clustering approaches suited to uncovering meaningful awareness profiles.

---

## Data Characteristics in This Project
- **Type**: Ordinal Likert responses aggregated into composite indices (e.g., concern, preparedness, responsibility), plus demographic/categorical features.  
- **Size/Dimensionality**: Moderate — 20 features, manageable for most clustering families.  
- **Nature**: Attitudinal, perceptual, and demographic data.  
- **Preprocessing already applied**: Dimensionality reduction by aggregation, creation of composite variables, removal of redundant items.  

---

## Data-Method Alignment for Climate Awareness

### High-Dimensional → Aggregated Survey Features
- The original 150+ Likert questions reflected **high-dimensional survey data**, which risked sparseness and interpretability issues. Aggregating into 20 composites addressed this challenge.  
- **Method implication**: With reduced dimensionality, algorithms like **K-means** or **hierarchical (Ward’s)** become practical. Factor analysis or PCA can still be used for visualization and validation.  

### Mixed Data Types → Ordinal + Demographics
- **Ordinal composites** (treated as scaled numerics) and **categorical demographics** (political preference, gender, age groups).  
- **Method implication**: For clustering, the main composites are central. Demographics are best reserved for post-hoc interpretation — ensuring clusters are defined by climate attitudes, then profiled by demographics afterwards. If demographics are included directly, **Gower distance + hierarchical clustering** could be tested.  

### Moderate Dimensionality → 20 Features
- With only 20 features, partitional and model-based methods are computationally efficient.  
- **Method implication**: **K-means/K-medoids** for interpretable centroids; **Gaussian Mixture Models** if overlap between groups is expected (e.g., people who are concerned yet disengaged).  

---

## Recommended Approaches
1. **K-means / K-medoids** → Clear centroid-based profiles of awareness and concern.  
2. **Hierarchical (Ward’s linkage)** → Exploration of nested structures (e.g., splitting “concerned” groups into active vs. passive).  
3. **Gaussian Mixture Models** → Capture overlapping identities (e.g., individuals partly skeptical yet showing solidarity traits).  
4. **Optional**: DBSCAN is less suitable here since data is not spatial and densities may not be distinct, but could flag small outlier groups (e.g., extreme skeptics).  

---

## Preprocessing Challenges in This Project
- **Scaling**: Ordinal composites on different ranges need standardization.  
- **Balance**: Composite variables (averages/sums) may outweigh single demographics — weighting strategy must be considered.  
- **Interpretability**: Ensuring clusters map back onto meaningful profiles for NGOs and policymakers.  

---

## Interpretation Strategy for Climate Awareness Profiles
- Use **composite indicators** (concern, preparedness, responsibility, solidarity, event experience) as the backbone of each cluster.  
- Demographics (age, political preference, education) will describe clusters post-hoc, giving each profile context and outreach relevance.  
- Label clusters as interpretable archetypes (e.g., “Concerned but Passive,” “Active Advocates,” “Skeptical/Disengaged,” etc.).  

---


The survey’s ordinal, composite-driven structure aligns best with **centroid-based and probabilistic clustering methods**, supported by hierarchical exploration. Documenting this alignment ensures every technical decision — preprocessing, algorithm choice, evaluation — stays tied to the project’s ultimate goal: mapping Italy’s climate mindscape to design more targeted communication and policy strategies.
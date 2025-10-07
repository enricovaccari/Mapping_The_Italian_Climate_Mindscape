# 🧭 Dimensionality Reduction Techniques — Decision Summary

This report compares **PCA**, **UMAP**, and **t-SNE** in terms of analytical suitability, interpretability, and computational efficiency.

## Decision Matrix

| Criterion | PCA | UMAP | t-SNE |
| --- | --- | --- | --- |
| Linear relationships | Excellent | Good | Poor |
| Non-linear relationships | Poor | Excellent | Excellent |
| Interpretability | High | Medium | Low |
| Computational speed | Fast | Medium | Slow |
| Large datasets | Excellent | Good | Poor |
| Clustering input | Excellent | Good | Fair |
| Visualization | Good | Excellent | Excellent |

---
### 🧩 Interpretation
- **PCA** → Best suited for *clustering input*, offering interpretability and stability.
- **UMAP** → Best for *non-linear visualization*, revealing structure PCA might miss.
- **t-SNE** → Strong local clustering for *fine-grained visualization*, but limited scalability.

### 🔍 Recommended Use in Pipeline
1. **PCA (90% variance)** → main clustering space.
2. **UMAP (2D)** → confirm global and local non-linear structure.
3. **t-SNE (2D)** → optional visual cross-check for local cohesion.

All methods converge on a consistent pattern: the dataset exhibits stable, interpretable clustering structure across both linear and non-linear projections.

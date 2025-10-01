# Mapping The Italian Climate Mindscape
Mapping the Italian Climate Mindscape explores public awareness and concern around climate change in Italy using data from the 2024 EIB Climate Survey.


---
Impact Certificate: Applied Machine Learning  
Challenge: Clustering  
Tomorrow University - Calibration Phase (Sep-Oct 2025)
Industry Focus: Social & Environmental  
Student: Enrico Vaccari 
---


### Problem Framing
Suppose some groups are highly concerned but inactive, while others underestimate risks altogether.  
- **Context**: Understanding these segments helps explain the awareness–action gap.  
- **Stakeholders**: Communication teams, educators, NGOs, policymakers.  
- **Impact**: More tailored strategies to close gaps between knowledge, concern, and action.  
- **Actionability**: Design differentiated messages and interventions for each cluster rather than relying on one-size-fits-all approaches. 

**Core questions** 
1. **Who** are you grouping? Italian citizens represented in the EIB Climate Survey.  
2. **What** patterns do you seek? Distinct awareness profiles that reveal how attitudes, concern and perceptions of climate change differ across the population.  
3. **Why** does it matter? Because knowing these profiles enables policymakers, NGOs and educators to design more targeted and effective communication strategies, helping close the gap between concern and action.  

This clarity shapes the technical path—guiding algorithm selection, feature treatment for ordinal survey data, and the criteria used to evaluate the usefulness of the resulting clusters.

**SMART Criteria**
- **Specific**: Segment Italian citizens by climate attitudes and awareness using survey data (EIB Climate Survey 2024).  
- **Measurable**: Identify a set of distinct awareness profiles (e.g., 4–6 clusters) characterized by attitudes, beliefs and demographic traits.  
- **Achievable**: The dataset consists of cleaned, Likert-scale responses from a representative sample of Italian residents; resources and clustering methods (KMeans, DBSCAN, Hierarchical) are available.  
- **Relevant**: Insights directly support NGOs, educators and policymakers in tailoring outreach strategies to close the awareness–action gap.  
- **Time-bound**: Conduct segmentation and deliver findings within the project timeframe (master’s capstone), with scope for extension into supervised predictive modeling in future iterations.  

**Problem Statement**  
> *Segment the Italian population by climate awareness and attitudes, using survey data, in order to identify distinct profiles that can inform targeted communication and policy strategies to close the gap between concern and action.*  
**Identify the Ultimate Goal**  
> *“Bridge the gap between climate concern and climate action in Italy, enabling more effective communication and policy responses.”*  


## Benefits

- **Current "one-size-fits-all" approach**  
  National campaigns and media messaging often treat the public as a homogeneous audience, emphasizing urgency without adapting to varying levels of concern, knowledge, or engagement.  

- **Three potential clusters** (there might be more)
  1. **Concerned but Passive** – Aware of climate risks, express high concern, but show low personal action.  
  2. **Skeptical or Disengaged** – Low concern, perceive climate change as distant or irrelevant.  
  3. **Active Advocates** – High awareness and active in adopting sustainable behaviors or advocating for policy change.  

- **Tailored interventions**  
  - Concerned but Passive → Focus on practical, low-barrier actions to bridge awareness and behavior.  
  - Skeptical or Disengaged → Use trust-building narratives and relatable local impacts to shift perceptions.  
  - Active Advocates → Empower them as multipliers through community leadership and peer-to-peer influence.  

- **Success metrics**  
  - Increased engagement rates (e.g., higher participation in climate initiatives or workshops).  
  - Improved alignment between reported concern and reported behavior.  
  - Broader public support for climate policies (measured through follow-up surveys or polls).  

### Capstone Connection
By documenting these expected benefits, the project makes clear why clustering is not just an academic exercise but a method to uncover actionable insights. These outcomes will serve as evaluation metrics for measuring the success and impact of the analysis.
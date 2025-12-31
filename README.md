# The 4AM Test: Official Happiness vs Hidden Distres

<div align="center">

[![Live Dashboard](https://img.shields.io/badge/Dashboard-Explore_Live-0EA5E9?style=for-the-badge&logo=plotly&logoColor=white)](https://70381211-90b5-4372-adaa-b7870c267fa1.plotly.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![Plotly](https://img.shields.io/badge/Built_with-Plotly-3F4F75?style=flat-square&logo=plotly)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)]()

**Comparing official happiness rankings with behavioral distress signals from late-night search patterns**

[Live Dashboard](https://70381211-90b5-4372-adaa-b7870c267fa1.plotly.app/) • [Methodology](#methodology) • [Data](#data-sources) • [Findings](#key-findings)

</div>

---

## Overview

Official happiness surveys rely on self-reported data where social desirability bias can influence responses. This research project analyzes the gap between OECD wellbeing scores and Google Trends search behavior for mental health distress signals across 16 countries.

**Research Question:** Do countries with high official happiness scores show corresponding low rates of distress-related searches?

---

## Key Findings

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Largest Gap** | Finland: 5.3 points | Official happiness (7.8/10) vs behavioral indicators |
| **Facade Countries** | 9 nations | Gap exceeds 3.0 points |
| **Highest Distress** | Mexico: 72.8 | Normalized search intensity |
| **Authentic Countries** | 3 nations | Gap < 2.0 (alignment between official and behavioral data) |

**High Gap Countries:** Finland (5.3), Netherlands (5.1), Denmark (5.0), Norway (4.6), Sweden (4.3)  
**Authentic Countries:** Australia (1.8), Switzerland (1.6), Germany (1.2)

---

## Interactive Dashboard

**[→ Explore the Interactive Dashboard](https://70381211-90b5-4372-adaa-b7870c267fa1.plotly.app/)**

Built with **[Plotly Studio](https://plotly.com/)**, the dashboard features:
- **Dual choropleth maps** comparing official vs behavioral data
- **Gap analysis visualizations** with interactive filtering
- **Country comparison tools** for head-to-head analysis
- **Temporal patterns** showing search intensity over time
- **Policy recommendations** based on data insights

*Special thanks to Plotly for providing the visualization platform and hosting infrastructure that made this research accessible.*

---

## Methodology

### Data Sources

#### 1. Google Trends API (Behavioral Data)
**Purpose:** Capture actual help-seeking behavior without survey bias

- **Search Terms:** `anxiety`, `depression`, `can't sleep`, `suicide hotline`, `burnout`
- **Period:** January 2024 - January 2025 (12 months)
- **Coverage:** 16 countries with complete datasets
- **Rationale:** Anonymous, aggregated search data reveals genuine distress patterns independent of social desirability bias

#### 2. OECD Better Life Index (Official Wellbeing)
**Purpose:** Standardized international happiness measurements

- **Metric:** Life satisfaction scores (0-10 scale)
- **Source:** [OECD Better Life Index](https://stats.oecd.org/Index.aspx?DataSetCode=BLI)
- **Rationale:** Provides the "official story" nations tell about citizen wellbeing through representative surveys

#### 3. WHO Mental Health Statistics (Clinical Validation)
**Purpose:** Independent clinical validation

- **Metrics:** Depression prevalence, suicide rates, anxiety disorder statistics
- **Source:** [WHO Mental Health Data](https://www.who.int/data/gho/data/themes/mental-health)
- **Rationale:** Clinical diagnoses offer third-party validation of mental health patterns

### Gap Calculation

```python
def calculate_gap(official_happiness, distress_score):
    """
    Calculate wellbeing gap between official claims and behavioral reality.
    
    Args:
        official_happiness: OECD score (0-10 scale)
        distress_score: Normalized Google Trends intensity (0-100)
    
    Returns:
        gap: Positive = facade, Negative = underselling
    """
    reality_score = 10 - (distress_score / 10)
    gap = official_happiness - reality_score
    return gap
```

**Classification:**
- `Gap < 0.0` → Underselling (more distressed than reported)
- `Gap 0.0-2.0` → Authentic (reality matches claims)
- `Gap 2.0-3.0` → Minor discrepancy
- `Gap > 3.0` → Facade (official claims exceed behavioral reality)

---



## Installation & Reproduction

```bash
# Clone repository
git clone https://github.com/[username]/the-4am-test.git
cd the-4am-test

# Install dependencies
pip install -r requirements.txt

# Reproduce analysis
python scripts/01_collect_trends.py    # Collect Google Trends data (~45-60 min)
python scripts/02_merge_datasets.py    # Merge datasets (~2-3 min)
python scripts/03_calculate_gap.py     # Calculate metrics (<1 min)
```

**Requirements:** Python 3.9+, pandas, numpy, requests

---

## Research Interpretations

Large gaps between official scores and behavioral data may indicate:

1. **Crisis Signal** – Actual mental health issues masked by social pressure to report positivity
2. **Awareness Indicator** – Successful destigmatization where people seek help openly
3. **Cultural Variance** – Different search behaviors across cultures independent of distress levels

**Key Insight:** Behavioral data should complement traditional surveys, not replace them. Large gaps warrant contextual investigation rather than immediate conclusions.

---

## Limitations

- Search behavior may reflect awareness rather than prevalence
- Cultural differences affect search patterns
- Internet access bias excludes some populations
- Data represents daily aggregates, not actual hourly patterns
- Limited to 16 countries with complete datasets
- Correlation ≠ causation

---

## Applications

| Audience | Use Case |
|----------|----------|
| **Policymakers** | Identify where official metrics may miss underlying issues; allocate resources based on behavioral signals |
| **Researchers** | Methodology for combining self-report with behavioral data in wellbeing studies |
| **Advocates** | Evidence for funding allocation; validates experiences in high-ranking countries |
| **Individuals** | Personal validation; awareness that struggles are reflected in population data |

---

## Citation

```bibtex
@misc{4am_test_2025,
  title={The 4AM Test: Official Happiness vs Hidden Distress},
  author={[Your Name]},
  year={2025},
  howpublished={\url{https://70381211-90b5-4372-adaa-b7870c267fa1.plotly.app/}},
  note={Analyzing gaps between official wellbeing surveys and behavioral distress signals}
}
```

---

## Contact

- **Live Dashboard:** https://70381211-90b5-4372-adaa-b7870c267fa1.plotly.app/
- **Email:** hanish.kumar9193@gmail.com
- **Issues:** [GitHub Issues](https://github.com/[username]/the-4am-test/issues)

---

## Acknowledgments

This project was built as part of the **Plotly Hackathon**.

Special thanks to:
- **[Plotly](https://plotly.com/)** for the visualization platform and hosting infrastructure
- **OECD** for open wellbeing data
- **Google Trends** for search analytics access
- **WHO** for mental health statistics

---

## Crisis Resources

If you or someone you know is struggling with mental health:

- **International:** https://findahelpline.com/
- **US Crisis Text Line:** Text HOME to 741741
- **UK Samaritans:** Call 116 123

Crisis support is available 24/7.

---

<div align="center">

**License:** MIT | **Status:** Active Research | **Last Updated:** January 2025

</div>

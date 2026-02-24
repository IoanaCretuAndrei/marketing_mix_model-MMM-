# Bayesian Marketing Mix Modeling (MMM) – Simulated Dataset

## Introduction

This project demonstrates a **Bayesian Marketing Mix Model (MMM)** to estimate the contribution of paid media channels on sales.  
Inspired by the Google MMM paper, it follows a professional workflow:

`spend → adstock → saturation → Bayesian model → contribution → ROAS → response curves`.

The goal is to analyze channel efficiency and optimize marketing budget allocation.

---

## Objectives

- Estimate the incremental contribution of **TV, YouTube, Facebook, and Search** on sales.
- Calculate **ROAS (Return on Ad Spend)** for each channel.
- Generate **response curves** to identify saturation points and optimize spend.
- Apply a professional MMM workflow using **transformations, Bayesian modeling, and visualizations**.

---

## Dataset

- Weekly simulated dataset with columns:

| Column | Description |
|--------|------------|
| date | Week start date |
| tv | Weekly TV spend |
| youtube | Weekly YouTube spend |
| facebook | Weekly Facebook spend |
| search | Weekly Search spend |
| sales | Weekly total sales |

> **Note:** Data is simulated for practice and visualization purposes.

---

## Transformations

1. **Adstock:** captures the carryover effect of each channel.

\[
Adstock_t = Spend_t + \theta \cdot Adstock_{t-1}
\]

2. **Saturation:** captures diminishing returns using lambda.

\[
Saturation = 1 - \exp(-\lambda \cdot Adstock)
\]

- Parameters used:

| Channel | Theta (Adstock) | Lambda (Saturation) |
|---------|----------------|-------------------|
| TV | 0.7 | 7.19e-6 |
| YouTube | 0.5 | 0.000196 |
| Facebook | 0.4 | 0.00036 |
| Search | 0.2 | 9.31e-5 |

> **Suggested plots:**  
> - Spend vs Adstock (`tv` vs `tv_adstock`)  
> - Adstock vs Saturation (`tv_adstock` vs `tv_sat`)

---

## Modeling

- Bayesian linear model using **PyMC**.
- Target: `sales`
- Features: `*_sat` (adstock + saturation)
- Outputs: posterior distributions of channel coefficients (`betas`) and weekly contributions.

> **Suggested plots:**  
> - Trace plots of betas  
> - Posterior distributions of coefficients

---

## Results

### Base vs Media Contribution

```text
Base sales: 59.3%
Media sales: 40.7%


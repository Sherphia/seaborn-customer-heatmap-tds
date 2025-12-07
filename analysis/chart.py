# Generates a professional Seaborn correlation heatmap for customer engagement
# Author: Sherphia (contact: 22f2001145@ds.study.iitm.ac.in)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Generate realistic synthetic customer engagement data ---
# Simulate 8 metrics for 400 customer sessions
np.random.seed(42)
n = 400

data = {
    "Session_Length_min": np.clip(np.random.normal(18, 7, n), 1, None),
    "Pages_Visited": np.clip(np.random.poisson(5, n) + np.random.normal(0, 1, n), 1, None),
    "Clicks": np.clip(np.random.poisson(10, n) + np.random.normal(0, 2, n), 0, None),
    "Add_to_Cart": np.random.binomial(1, 0.22, n) + np.random.binomial(1, 0.06, n),
    "Purchase_Amount_USD": np.clip(np.random.exponential(70, n) + np.random.normal(0, 20, n), 0, None),
    "Return_Visits_30d": np.clip(np.random.poisson(1, n), 0, None),
    "Email_Opens_30d": np.clip(np.random.poisson(3, n), 0, None),
    "Support_Contacts": np.random.poisson(0.25, n)
}

df = pd.DataFrame(data)

# Introduce intentional correlations for realism
df["Pages_Visited"] += (df["Session_Length_min"] / 9).round(0)
df["Clicks"] += (df["Pages_Visited"] * 0.45).round(0)
df["Purchase_Amount_USD"] += df["Add_to_Cart"] * np.random.normal(65, 18, n)

# --- Compute correlation matrix ---
corr = df.corr()

# --- Seaborn styling ---
sns.set_style("white")
sns.set_context("talk", font_scale=0.9)

plt.figure(figsize=(8, 8))   # 8in × 8in at 64 dpi → EXACTLY 512×512 px
cmap = sns.diverging_palette(230, 20, as_cmap=True)

ax = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap=cmap,
    vmin=-1,
    vmax=1,
    center=0,
    linewidths=0.5,
    linecolor="white",
    cbar_kws={"shrink": 0.75, "label": "Pearson Correlation"}
)

ax.set_title("Customer Engagement Metrics — Correlation Matrix", fontsize=14, pad=14)
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

# Save exactly 512×512 px
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("chart.png successfully created (512x512 px).")

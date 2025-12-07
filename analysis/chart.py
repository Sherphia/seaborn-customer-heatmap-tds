import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Synthetic customer engagement data
np.random.seed(42)
data = pd.DataFrame({
    "Page_Views": np.random.normal(40, 10, 200),
    "Clicks": np.random.normal(15, 5, 200),
    "Time_On_Site": np.random.normal(300, 60, 200),
    "Purchases": np.random.normal(5, 2, 200),
    "Email_Opens": np.random.normal(20, 7, 200),
    "Returns": np.random.normal(2, 1, 200)
})

corr = data.corr()

# FIXED 512x512 EXACT
plt.figure(figsize=(8, 8), dpi=64)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    square=True
)

plt.title("Customer Engagement Correlation Matrix", fontsize=18)

# SAVE WITHOUT bbox_inches
plt.savefig("chart.png")
plt.close()

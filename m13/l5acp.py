import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# Load dataset
# ==============================
data = pd.read_csv("FuelConsumption.csv")

# ==============================
# 1. Null values check + handling
# ==============================
print("Null values:\n", data.isnull().sum())

data.fillna(data.median(numeric_only=True), inplace=True)

# ==============================
# 2. Dataset details
# ==============================
print("\nDataset Info:")
print(data.info())

# ==============================
# 3. Countplot with different themes
# ==============================

themes = ["white", "dark", "whitegrid", "darkgrid", "ticks"]

for theme in themes:
    sns.set_style(theme)

    plt.figure(figsize=(6,4))
    sns.countplot(x="FUELTYPE", data=data, palette="viridis")

    plt.title(f"Fuel Type Countplot - Theme: {theme}")
    plt.xticks(rotation=45)
    plt.show()

# ==============================
# 4. White theme + remove spines
# ==============================
sns.set_style("white")

plt.figure(figsize=(6,4))
ax = sns.countplot(x="FUELTYPE", data=data, palette="coolwarm")

# remove spines
sns.despine()

plt.title("Fuel Type Countplot (White Theme, No Spines)")
plt.xticks(rotation=45)
plt.show()

# ==============================
# 5. Palette + bar color customization
# ==============================
sns.set_style("whitegrid")

plt.figure(figsize=(6,4))
sns.countplot(x="FUELTYPE", data=data, color="orange")  # custom bar color

plt.title("Fuel Type Countplot (Custom Bar Color)")
plt.xticks(rotation=45)
plt.show()

# ==============================
# 6. Figure scaling (paper, notebook, talk, poster)
# ==============================
scales = ["paper", "notebook", "talk", "poster"]

for scale in scales:
    sns.set_context(scale, font_scale=1 if scale != "poster" else 0.8)

    plt.figure(figsize=(6,4))
    sns.countplot(x="FUELTYPE", data=data, palette="Set2")

    plt.title(f"Context Scaling: {scale}")
    plt.xticks(rotation=45)
    plt.show()

# ==============================
# 7. Final styled plot (combination)
# ==============================
sns.set_theme(style="whitegrid", palette="pastel", context="poster", font_scale=0.8)

plt.figure(figsize=(8,5))
sns.countplot(x="FUELTYPE", data=data)

plt.title("Final Styled Fuel Type Countplot")
plt.xticks(rotation=45)
plt.show()
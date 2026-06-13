import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load dataset
# -----------------------------
data = pd.read_csv("FuelConsumption.csv")

# -----------------------------
# 2. Check null values
# -----------------------------
print("Missing values per column:\n")
print(data.isnull().sum())

# Handle missing values (safe cleanup)
data = data.dropna()

# -----------------------------
# 3. Dataset details
# -----------------------------
print("\nDataset Info:\n")
print(data.info())

print("\nStatistical Summary:\n")
print(data.describe())

# -----------------------------
# 4. Group by FUELTYPE (mean)
# -----------------------------
grouped_df = data.groupby("FUELTYPE").mean(numeric_only=True)

# Reset index
grouped_df = grouped_df.reset_index()

print("\nGrouped Data (Fuel Type vs CO2):\n")
print(grouped_df[["FUELTYPE", "CO2EMISSIONS"]])

# -----------------------------
# 5. Barplot
# -----------------------------
plt.figure(figsize=(8,5))

plot = sns.barplot(
    x="FUELTYPE",
    y="CO2EMISSIONS",
    data=grouped_df,
    color="teal"
)

# -----------------------------
# 6. Annotate bars
# -----------------------------
for bar in plot.patches:
    plot.annotate(
        format(bar.get_height(), ".2f"),
        (bar.get_x() + bar.get_width()/2, bar.get_height()),
        ha="center",
        va="bottom",
        fontsize=10,
        xytext=(0, 5),
        textcoords="offset points"
    )

plt.title("Average CO2 Emissions by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average CO2 Emissions")
plt.show()
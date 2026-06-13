import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("FuelConsumption.csv")
print(data.head())

print(data.isnull().sum())

data.fillna(data.median(numeric_only=True), inplace=True)

print(data.info())
print(data.describe())

fuel_counts = data['FUELTYPE'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    fuel_counts,
    labels=fuel_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops={'edgecolor': 'black', 'linewidth': 2}
)

plt.title("Fuel Type Distribution")
plt.show()

vehicle_counts = data['VEHICLECLASS'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(
    vehicle_counts,
    labels=vehicle_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)

plt.title("Vehicle Class Distribution")
plt.show()


plt.figure(figsize=(12,5))

plt.plot(data['CO2EMISSIONS'], color='green')

plt.xlabel("Index")
plt.ylabel("CO2 Emissions")
plt.title("CO2 Emissions Trend")
plt.grid(True)

plt.show()
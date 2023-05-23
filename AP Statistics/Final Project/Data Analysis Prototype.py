import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Documents/AP Statistics/Final Project/dataset.csv')

# Overview of the dataset
print("Dataset Overview:")
print(data.head())
print("\n")

# Basic statistical analysis
print("Basic Statistics:")
print(data.describe())
print("\n")

# Data cleaning and preprocessing
print("Data Cleaning:")
# Define the important columns
important_cols = ['name', 'reclat', 'reclong', 'mass (g)', 'year', 'fall']
# Check if all important columns exist in the dataset
missing_cols = list(set(important_cols) - set(data.columns))
if missing_cols:
    print("Missing columns:", missing_cols)
    exit()
# Remove rows with missing values in important columns
data = data.dropna(subset=important_cols)
# Convert year column to numeric type
data['year'] = pd.to_numeric(data['year'], errors='coerce')
print("Number of rows after cleaning:", len(data))
print("\n")

# Statistical analysis
print("Statistical Analysis:")
# Correlation matrix
corr_matrix = data[['mass (g)', 'year']].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
print("\n")

# Histogram of mass (g)
plt.figure(figsize=(8, 6))
plt.hist(data['mass (g)'], bins=30, edgecolor='black')
plt.xlabel('Mass (g)')
plt.ylabel('Frequency')
plt.title('Distribution of Meteorite Mass')
plt.show()
print("\n")

# Scatter plot of mass (g) vs. year
plt.figure(figsize=(8, 6))
plt.scatter(data['year'], data['mass (g)'], alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Mass (g)')
plt.title('Meteorite Mass over Time')
plt.show()
print("\n")

# Box plot of fall vs. mass (g)
plt.figure(figsize=(8, 6))
sns.boxplot(x='fall', y='mass (g)', data=data)
plt.xlabel('Fall')
plt.ylabel('Mass (g)')
plt.title('Mass of Fallen and Found Meteorites')
plt.show()
print("\n")

# Additional advanced analysis and visualizations
# Example: Bar chart of the top 10 meteorite classes
top_classes = data['recclass'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_classes.index, y=top_classes.values, palette='cool')
plt.xticks(rotation=45)
plt.xlabel('Meteorite Class')
plt.ylabel('Count')
plt.title('Top 10 Meteorite Classes')
plt.show()
print("\n")

# Save the cleaned dataset
data.to_csv('cleaned_meteorite_landings.csv', index=False)

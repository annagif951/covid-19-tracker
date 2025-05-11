import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv("covid_data.csv")  # Replace with your dataset
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'covid_data.csv' was not found.")
    df = pd.DataFrame()  # Create an empty DataFrame as a fallback

# Display the first 10 rows of the dataset
print("First 10 rows of the dataset:")
print(df.head(10))

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Provide summary statistics
print("\nSummary statistics:")
print(df.describe())

# Convert the 'date' column to datetime format
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Handle invalid dates
    print("\nConverted 'date' column to datetime format.")

# Sort the dataset by date
if 'date' in df.columns:
    df.sort_values(by='date', inplace=True)
    print("\nDataset sorted by 'date' column.")

# Data cleaning: Remove rows with missing values
df.dropna(inplace=True)
print("\nRemoved rows with missing values.")

# Display the cleaned dataset
print("\nCleaned dataset:")
print(df.head(10))

plt.figure(figsize=(10,5))
sns.lineplot(x='date', y='cases', data=df)
plt.title('COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.show()
# Display the last 10 rows of the dataset
print("\nLast 10 rows of the dataset:")
df.to_csv("processed_covid_data.csv", index=False)  # Save cleaned dataset

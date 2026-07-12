import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/twitter_training.csv", header=None)

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Assign column names
df.columns = ["ID", "Entity", "Sentiment", "Text"]

# Display column names
print("\nColumn Names:")
print(df.columns)

# Dataset information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Sentiment distribution
print("\nSentiment Distribution:")
print(df["Sentiment"].value_counts())

# Plot sentiment distribution
df["Sentiment"].value_counts().plot(
    kind="bar",
    figsize=(8,5),
    title="Sentiment Distribution"
)

plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
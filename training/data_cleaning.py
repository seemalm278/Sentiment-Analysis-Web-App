import re
import string
import os
import pandas as pd

print("Loading dataset...")

df = pd.read_csv("dataset/twitter_training.csv", header=None)

df.columns = ["ID", "Entity", "Sentiment", "Text"]

print("Dataset loaded successfully!")

# Remove empty rows
df = df.dropna(subset=["Text"])

def clean_text(text):

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML
    text = re.sub(r"<.*?>", "", text)

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


print("Cleaning text...")

df["Clean_Text"] = df["Text"].apply(clean_text)

print("\nOriginal Text:")
print(df["Text"].head())

print("\nCleaned Text:")
print(df["Clean_Text"].head())

output_path = "dataset/cleaned_twitter.csv"

df.to_csv(output_path, index=False)

print("\nFile saved successfully!")
print("Saved at:", os.path.abspath(output_path))
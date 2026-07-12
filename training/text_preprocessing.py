import re
import pandas as pd
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download NLTK resources (only needed the first time)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

print("Loading cleaned dataset...")

df = pd.read_csv("dataset/cleaned_twitter.csv")

print("Dataset loaded successfully!")

# Initialize tools
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = str(text).lower()

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    tokens = [stemmer.stem(word) for word in tokens]

    # Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return " ".join(tokens)

print("Processing text...")

df["Processed_Text"] = df["Clean_Text"].apply(preprocess_text)

print("\nOriginal:")
print(df["Clean_Text"].head())

print("\nProcessed:")
print(df["Processed_Text"].head())

# Save dataset
output_path = "dataset/preprocessed_twitter.csv"

df.to_csv(output_path, index=False)

print("\nPreprocessed dataset saved successfully!")
print("Saved at:", output_path)
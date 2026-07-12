import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

print("Loading preprocessed dataset...")

df = pd.read_csv("dataset/preprocessed_twitter.csv")

print("Dataset loaded successfully!")

# Remove rows with missing values
df = df.dropna(subset=["Processed_Text", "Sentiment"])

# Features (X)
X = df["Processed_Text"]

# Labels (y)
y = df["Sentiment"]

print("\nCreating TF-IDF vectors...")

vectorizer = TfidfVectorizer(max_features=5000)

X_vectorized = vectorizer.fit_transform(X)

print("Vectorization Complete!")

print("\nFeature Matrix Shape:")
print(X_vectorized.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", X_train.shape[0])
print("Testing Samples :", X_test.shape[0])

print("\nFeature Engineering Completed Successfully!")
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split

print("Loading dataset...")

# Load dataset
df = pd.read_csv("dataset/preprocessed_twitter.csv")

# Remove missing values
df = df.dropna(subset=["Processed_Text", "Sentiment"])

# Remove the "Irrelevant" class so the model predicts only:
# Positive, Negative, Neutral
df = df[df["Sentiment"] != "Irrelevant"]

print("Dataset loaded successfully!")

# Features and labels
X = df["Processed_Text"]
y = df["Sentiment"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Logistic Regression model...")

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model trained successfully!")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print(f"Accuracy: {accuracy * 100:.2f}%")
print("==============================")

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "backend/model.pkl")
joblib.dump(vectorizer, "backend/vectorizer.pkl")

print("\nModel saved successfully!")
print("backend/model.pkl")
print("backend/vectorizer.pkl")
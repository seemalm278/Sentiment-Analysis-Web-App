from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# Create FastAPI app
app = FastAPI(title="Sentiment Analysis API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
model = joblib.load("backend/model.pkl")
vectorizer = joblib.load("backend/vectorizer.pkl")


class TextInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Sentiment Analysis API is Running"
    }


@app.post("/predict")
def predict(data: TextInput):

    # Convert text into TF-IDF features
    vector = vectorizer.transform([data.text])

    # Predict sentiment
    prediction = model.predict(vector)[0]

    return {
        "text": data.text,
        "prediction": prediction
    }
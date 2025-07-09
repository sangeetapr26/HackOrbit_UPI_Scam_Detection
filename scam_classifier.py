from transformers import pipeline
from utils import SCAM_KEYWORDS

# Load classifier once
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def detect_scam_indicators(text):
    text_lower = text.lower()
    return [kw for kw in SCAM_KEYWORDS if kw in text_lower]

def classify_text(text):
    result = classifier(text[:512])[0]  # Truncate to 512 tokens
    scam_score = round(result['score'] * 100) if result['label'] == 'NEGATIVE' else 100 - round(result['score'] * 100)
    return scam_score

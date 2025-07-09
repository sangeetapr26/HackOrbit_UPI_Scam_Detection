from scam_classifier import detect_scam_indicators, classify_text
from utils import SCAM_KEYWORDS

def assess_risk(text):
    # Step 1: Detect scam-related keywords present in text
    red_flags = [kw for kw in SCAM_KEYWORDS if kw.lower() in text.lower()]

    # Step 2: Calculate keyword-based risk score (capped to max 6 points)
    keyword_score = sum(SCAM_KEYWORDS[kw] for kw in red_flags)
    keyword_score = min(keyword_score, 6)  # Prevents inflation

    # Step 3: Get AI NLP model's scam probability (0–100)
    scam_score_ai = classify_text(text)

    # Step 4: Blend both scores softly
    final_score = (scam_score_ai * 0.4) + (keyword_score * 3)
    final_score = min(round(final_score), 100)

    # Step 5: Suggest action based on final score
    if final_score >= 85:
        suggestion = "BLOCK – High Risk"
    elif final_score >= 55:
        suggestion = "Verify Before Proceeding"
    else:
        suggestion = "Proceed"

    return {
        "scam_score": final_score,
        "red_flags": red_flags,
        "suggestion": suggestion
    }

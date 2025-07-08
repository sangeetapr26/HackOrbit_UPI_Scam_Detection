SCAM_KEYWORDS = [
"Important information", "urgent", "verify", "OTP","immediately", "lucky winner",
    "verify now", "KYC", "SBI helpdesk", "govt scheme", "pay now", "crypto currency",
    "reward", "cashback", "bonus", "refund", "win now", "free money", "lottery",
    "jackpot", "KYC update", "verify account", "account suspended", "bank blocked",
    "urgent", "immediately", "last chance", "limited time", "scan to receive",
    "official support", "click this link", "remote access", "legal action", "fine",
    "FIR issued", "sarkari yojana", "bhim app", "modi yojana", "pension scheme","only 1 hour left","cashback",
    "support","relief","win ₹1000 / win now","claim your prize","account issue","account suspended","collect request","click this link",
    "scan to receive","QR code expired","official support","customer care number","remote access","My11 Circle","upgrade the system",
    "earned","FREE","deposit","claim your coupon","mega contest","Do not share this code"
    "limited time","amazing offer"
]

def detect_scam_keywords(text):
    text_lower = text.lower()
    return [kw for kw in SCAM_KEYWORDS if kw in text_lower]

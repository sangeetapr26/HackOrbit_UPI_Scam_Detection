UPI Scam Detector:

This project implements a UPI (Unified Payments Interface) scam detection system that analyzes screenshots of UPI transactions or suspicious messages to identify potential scams. It leverages OCR for image-to-text extraction, an NLP model for text classification, and a keyword-based risk assessment to provide a comprehensive scam score and suggested action.

Features:

1. Screenshot Analysis: Upload UPI transaction screenshots, and the system will extract text using OCR.
2. Message Analysis: Paste suspicious text messages directly for analysis.
3. Keyword Detection: Identifies common scam-related keywords and assigns a score based on their risk level.
4. AI-Powered NLP Classification: Utilizes a pre-trained distilbert-base-uncased-finetuned-sst-2-english model to classify text and determine a scam probability.
5. Blended Risk Assessment: Combines keyword scores and AI model probability to generate a final scam score (0-100).
6. Actionable Suggestions: Provides clear suggestions based on the final scam score: "BLOCK - High Risk", "Verify Before Proceeding", or "Proceed".

Project Structure:

upi_scam_detector/
│

├── app.py                        # Flask web server

├── ocr.py                        # OCR + QR code extractor

├── scam_classifier.py            # AI text classification

├── risk_assesment.py             # Combines AI and keyword scores

├── utils.py                      # Scam keyword database

│

├── static/

│   ├── uploads/                   # Uploaded screenshots

│   ├── style.css                  # Optional custom CSS

│   └── script.js                  # Client-side validation

│

├── templates/

│   └── index.html                  # Main web UI

│
├── requirements.txt

└── README.md                       # 📄 here!


The project is organized into several Python modules and a Flask web application:

1. requirements.txt: Lists all necessary Python dependencies.
2. ocr.py: Handles Optical Character Recognition (OCR) to extract text from images and QR code data.
3. scam_classifier.py: Contains the logic for loading the NLP text classification model and detecting scam indicators.
4. utils.py: Defines a dictionary of SCAM_KEYWORDS with associated risk scores and a function to detect these keywords in text.
5. risk_assesment.py: Implements the core risk assessment logic, blending keyword scores and AI-generated scam probabilities.
6. app.py: The main Flask application that handles web requests, file uploads, text processing, and rendering of results.
7. indec.html: The front-end HTML template for the web interface, allowing users to upload screenshots or paste messages.
8. script.js: Frontend JavaScript for basic form handling and user experience improvements.
9. static/style.css: (Implied) Custom CSS for styling the web application.

Setup and Installation:
To set up and run the UPI Scam Detector, follow these steps:

1. Prerequisites
Python 3.x

2. tesseract-ocr installed on your system. Make sure the path to tesseract.exe is correctly set in OCR.py (e.g., pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe').

3. Install Dependencies
Install the required Python packages using pip:
pip install -r REQUIREMENT.TXT
The REQUIREMENT.TXT file includes:
pytesseract
Pillow
pyzbar
transformers
torch
scikit-learn

4. Run the Application
Navigate to the project's root directory and run the Flask application:
python APP.py
The application will typically run on http://127.0.0.1:5000/. Open this URL in your web browser.

Usage:

1. Access the Web Interface: Open your web browser and go to the address where the Flask app is running (e.g., http://127.0.0.1:5000/).
2. Upload Screenshot: Click on "Upload Screenshot" and select a UPI transaction screenshot from your device.
3. Or Paste Message: Alternatively, paste any suspicious message into the "Or Paste Message" text area.
4. Analyze: Click the "Analyze" button.
5. View Results: The page will display the "Analysis Results"
6. Including:
   
  i. Scam Score: A percentage indicating the likelihood of a scam.
   
  ii. Suggestion: A recommended action (BLOCK - High Risk, Verify Before Proceeding, or Proceed).
  
 iii. Flags Detected: A list of keywords identified as red flags.
 
  iv. Extracted Text: The full text extracted from the screenshot or the message you provided.
  

How it Works:

1. The system processes input (screenshot or message) through the following pipeline:

2. Text Extraction:
   
     i. If a screenshot is uploaded, OCR.py uses pytesseract to extract text from the image.
   
     ii. If a message is pasted, it's used directly.

4. Risk Assessment (RISK_ASSESSMENT.py):
   
      i. Keyword Detection: detect_scam_keywords from UTILS.py identifies predefined scam keywords in the extracted text.
   
     ii. Keyword Score: A keyword_score is calculated based on the risk points assigned to each detected keyword (capped at 6 points to prevent inflation).

6. AI Scam Probability: classify_text from SCAM_CLASSIFIER.py uses a distilbert based NLP model to determine an AI-driven scam probability (0-100). The text is truncated to 512 tokens for the model.

7. Final Score Blending: The final_score is calculated by blending the AI scam probability and the keyword score 

     using the formula:

     final_score=(scam_score_ai×0.4)+(keyword_score×3)
     The final score is rounded and capped at 100.

8. Suggestion Generation: Based on the final_score:

      geq85: "BLOCK - High Risk"

      geq55: "Verify Before Proceeding"

      \<55: "Proceed"

9. Dependencies:

   The REQUIREMENT.TXT file lists the Python libraries needed for this project. Ensure they are installed before running the application.

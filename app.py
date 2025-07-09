from flask import Flask, render_template, request
#import streamlit as st
from ocr import extract_text_from_image, extract_qr_data
from risk_assesment import assess_risk  
from utils import detect_scam_keywords
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    extracted_text = ""
    
    if request.method == "POST":
        file = request.files.get("screenshot")
        message = request.form.get("message")

        if file and file.filename:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            extracted_text = extract_text_from_image(path)
        elif message:
            extracted_text = message

        result = assess_risk(extracted_text)

    return render_template("index.html", result=result, extracted_text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)

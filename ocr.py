import cv2
import numpy as np
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def extract_qr_data(image_path):
    image = cv2.imread(image_path)
    qr_decoder = cv2.QRCodeDetector()
    data, points, _ = qr_decoder.detectAndDecode(image)
    return [data] if data else []

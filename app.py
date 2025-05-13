from flask import Flask, request
from textract_functions.detect_document_text import detect_document_text
from textract_functions.analyze_document import analyze_document
from openAI_functions.interpret_text import interpret_text
from routes.extract_data_from_image import extract_data_from_image
from authentication_functions.signin_existing_user import signin_with_email_password
from authentication_functions.signup_new_user import signup_with_email_password, signup_with_phone_password

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get():
    return "Hello, client!"

@app.route("/ddt", methods=["POST"])
def ddt():
    response = detect_document_text(request)
    return response

@app.route("/analyze", methods=["POST"])
def analyze():
    response = analyze_document(request)
    return response

@app.route("/interpret", methods=["POST"])
def interpret():
    response = interpret_text(request)
    return response

@app.route("/extract_and_interpret", methods=["POST"])
def extract_and_interpret():
    response = extract_data_from_image(request)
    return response

@app.route('/signin_with_email', methods=['POST'])
def signin_existing_email():
    response = signin_with_email_password(request)
    return response

@app.route('/signup_with_email', methods=['POST'])
def signup_new_email():
    response = signup_with_email_password(request)
    return response

@app.route('/signup_with_phone', methods=['POST'])
def signup_new_phone():
    response = signup_with_phone_password(request)
    return response
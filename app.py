from flask import Flask, request
from textract_functions.detect_document_text import detect_document_text
from textract_functions.analyze_document import analyze_document
from openAI_functions.interpret_text import interpret_text


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

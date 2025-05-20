from flask import Flask, request, abort
from textract_functions.detect_document_text import detect_document_text
from textract_functions.analyze_document import analyze_document
from openAI_functions.interpret_text import interpret_text
from openAI_functions.analyze_image import analyze_image
from routes.extract_data_from_image import extract_data_from_image
from routes.get_user import get_user_from_session
from routes.add_confirmation import add_confirmation_route
from routes.get_confirmations import (
    get_active_confirmations_by_user,
    get_all_confirmations_by_user,
    get_inactive_confirmations_by_user,
)
import json
from werkzeug.exceptions import HTTPException
from authentication_functions.signin_existing_user import (
    signin_with_email_password,
    signin_with_phone_password,
)
from authentication_functions.signup_new_user import (
    signup_with_email_password,
    signup_with_phone_password,
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get():
    return "Hello, client!"


@app.route("/openAI_image_analysis", methods=["POST"])
def openAI_image_analysis():
    response = analyze_image(request)
    return response


@app.route("/signin/email", methods=["POST"])
def signin_existing_email():
    response = signin_with_email_password(request)

    if response.session:
        return {
            "message": "Signin successful",
            "access_token": response.session.access_token,
        }
    else:
        return response


@app.route("/signin/phone", methods=["POST"])
def signin_existing_phone():
    response = signin_with_phone_password(request)

    if response.session:
        return "Signin successful"
    else:
        return response


@app.route("/signup/email", methods=["POST"])
def signup_new_email():
    response = signup_with_email_password(request)

    # if response.session:
    #     return "Signup successful"
    # else:
    return response


@app.route("/signup/phone", methods=["POST"])
def signup_new_phone():
    response = signup_with_phone_password(request)

    if response.session:
        return "Signup successful"
    else:
        return response


@app.route("/confirmations/add", methods=["POST"])
def add_confirmation():
    """Add confirmation."""
    return add_confirmation_route(request)


@app.route("/confirmations/all", methods=["GET"])
def get_all_confirmations():
    """Get all confirmations."""
    return get_all_confirmations_by_user(request)


@app.route("/confirmations/active", methods=["GET"])
def get_active_confirmations():
    """Get active confirmations."""
    return get_active_confirmations_by_user(request)


@app.route("/confirmations/inactive", methods=["GET"])
def get_inactive_confirmations():
    """Get inactive confirmations."""
    return get_inactive_confirmations_by_user(request)


@app.route("/test_error", methods=["GET"])
def test_error():
    """Test error handling."""
    abort(409, description="This is a test error.")


@app.errorhandler(HTTPException)
def handle_exception(e):
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


# @app.route("/ddt", methods=["POST"])
# def ddt():
#     response = detect_document_text(request)
#     return response


# @app.route("/extract", methods=["POST"])
# def extract():
#     response = analyze_document(request)
#     return response


# @app.route("/interpret", methods=["POST"])
# def interpret():
#     response = interpret_text(request)
#     return response


# @app.route("/extract_and_interpret", methods=["POST"])
# def extract_and_interpret():
#     response = extract_data_from_image(request)
#     return response

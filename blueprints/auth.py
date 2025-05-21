from flask import Blueprint, request
from routes.auth.signin import (
    signin_with_email_password,
    signin_with_phone_password,
)
from routes.auth.signup import (
    signup_with_email_password,
    signup_with_phone_password,
)


AUTH_BLUEPRINT = Blueprint("auth", __name__, url_prefix="/auth")


@AUTH_BLUEPRINT.route("/signin/email", methods=["POST"])
def signin_existing_email():
    response = signin_with_email_password(request)

    if response.session:
        return {
            "message": "Signin successful",
            "access_token": response.session.access_token,
        }
    else:
        return response


@AUTH_BLUEPRINT.route("/signin/phone", methods=["POST"])
def signin_existing_phone():
    response = signin_with_phone_password(request)

    if response.session:
        return "Signin successful"
    else:
        return response


@AUTH_BLUEPRINT.route("/signup/email", methods=["POST"])
def signup_new_email():
    response = signup_with_email_password(request)

    # if response.session:
    #     return "Signup successful"
    # else:
    return response


@AUTH_BLUEPRINT.route("/signup/phone", methods=["POST"])
def signup_new_phone():
    response = signup_with_phone_password(request)

    if response.session:
        return "Signup successful"
    else:
        return response

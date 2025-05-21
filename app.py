from flask import Flask, request, abort
import json
from werkzeug.exceptions import HTTPException
from blueprints.confirmations import CONFIRMATIONS_BLUEPRINT
from blueprints.auth import AUTH_BLUEPRINT

app = Flask(__name__)
app.register_blueprint(CONFIRMATIONS_BLUEPRINT)
app.register_blueprint(AUTH_BLUEPRINT)


@app.route("/", methods=["GET"])
def get():
    return "Hello, client!"


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

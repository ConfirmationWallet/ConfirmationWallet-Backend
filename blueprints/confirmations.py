from flask import Blueprint, request
from routes.confirmations.add_confirmation import add_confirmation_route
from routes.confirmations.get_confirmations import (
    get_all_confirmations_by_user,
    get_active_confirmations_by_user,
    get_inactive_confirmations_by_user,
)


CONFIRMATIONS_BLUEPRINT = Blueprint(
    "confirmations", __name__, url_prefix="/confirmations"
)


@CONFIRMATIONS_BLUEPRINT.route("/add", methods=["POST"])
def add_confirmation():
    """Add confirmation."""
    return add_confirmation_route(request)


@CONFIRMATIONS_BLUEPRINT.route("/all", methods=["GET"])
def get_all_confirmations():
    """Get all confirmations."""
    return get_all_confirmations_by_user(request)


@CONFIRMATIONS_BLUEPRINT.route("/active", methods=["GET"])
def get_active_confirmations():
    """Get active confirmations."""
    return get_active_confirmations_by_user(request)


@CONFIRMATIONS_BLUEPRINT.route("/inactive", methods=["GET"])
def get_inactive_confirmations():
    """Get inactive confirmations."""
    return get_inactive_confirmations_by_user(request)

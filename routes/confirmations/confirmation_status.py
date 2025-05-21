from primary_functions.helper_functions.mongodb import (
    activate_confirmation,
    deactivate_confirmation,
)
from primary_functions.authentication.get_user import get_user_from_session


def activate_confirmation_route(request):
    user = get_user_from_session(request)
    if not user:
        return {"error": "User not found"}, 401
    confirmation_id = request.body.get("confirmation_id")
    if not confirmation_id:
        return {"error": "Confirmation ID not provided"}, 400

    result = activate_confirmation(confirmation_id)

    if result:
        return {"message": "Confirmation activated successfully"}, 200
    else:
        return {"error": "Failed to activate confirmation"}, 500


def activate_confirmation_route(request):
    user = get_user_from_session(request)
    if not user:
        return {"error": "User not found"}, 401
    confirmation_id = request.body.get("confirmation_id")
    if not confirmation_id:
        return {"error": "Confirmation ID not provided"}, 400

    result = deactivate_confirmation(confirmation_id)

    if result:
        return {"message": "Confirmation deactivated successfully"}, 200
    else:
        return {"error": "Failed to deactivate confirmation"}, 500

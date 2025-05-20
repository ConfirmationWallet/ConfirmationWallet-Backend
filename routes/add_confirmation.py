from helper_functions.mongodb import add_confirmation
from helper_functions.supabase import get_user_from_session
from helper_functions.openAI import format_openai_response
from openAI_functions.analyze_image import analyze_image
import json


def add_confirmation_route(request):
    user = get_user_from_session(request)
    if not user:
        return {"error": "User not found"}, 401
    image_analysis_text = analyze_image(request)
    confirmation_data = format_openai_response(image_analysis_text)

    if confirmation_data.get("error"):
        return confirmation_data, 400

    confirmation_data["user"] = user.id

    confirmation_id = add_confirmation(confirmation_data, user)
    return {"confirmation_id": str(confirmation_id)}, 200

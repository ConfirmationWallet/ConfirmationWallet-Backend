import json
from datetime import datetime


def format_openai_response(openai_response_string):
    """
    Formats the OpenAI response to a JSON object.
    """
    # Check if the response is valid JSON
    try:
        openai_response_dict = json.loads(openai_response_string)
    except json.JSONDecodeError:
        # If the response is not valid JSON, return an error message
        return {"error": "Invalid JSON response from OpenAI."}

    if openai_response_dict.get("error"):
        # If the response contains an error, return it
        return {"error": openai_response_dict["error"]}

    formatted_response = {"active": True}
    required_fields = [
        "booking_date",
        "event_date",
        "event_time",
        "email",
        "confirmation_number",
        "details",
    ]

    # Iterate through the keys in the OpenAI response
    for key, value in openai_response_dict.items():

        if value == "not found":
            formatted_response[key] = None
            continue

        if key in required_fields:
            # If the key is in the required fields, add it to the formatted response
            if key == "booking_date" or key == "event_date" or key == "event_time":
                # Convert the date strings to datetime objects
                formatted_response[key] = datetime.fromisoformat(value)
            else:
                formatted_response[key] = value
        else:
            # If the key is not in the required fields, add it to the details field
            if "details" not in formatted_response:
                formatted_response["details"] = {}
            formatted_response["details"][key] = value

    print("Formatted OpenAI response:", formatted_response)

    return formatted_response

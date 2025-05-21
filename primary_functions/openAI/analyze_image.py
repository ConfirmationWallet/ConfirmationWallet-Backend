import json
import base64
from primary_functions.helper_functions.openAI import get_openai_client
from constants.openAI_constants import OPENAI_ONLY_SYSTEM_PROMPT


def analyze_image(request):
    image = request.files["image"]
    image_data = image.read()
    image_base64 = base64.b64encode(image_data).decode("utf-8")

    client = get_openai_client()
    response = client.responses.create(
        model="o4-mini",
        input=[
            {
                "role": "developer",
                "content": [
                    {
                        "type": "input_text",
                        "text": f"{OPENAI_ONLY_SYSTEM_PROMPT}",
                    },
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_base64}",
                    },
                ],
            },
        ],
    )
    print("OPENAI IMAGE ANALYSIS")
    print("total tokens: ", response.usage.total_tokens)
    print("prompt tokens: ", response.usage.input_tokens)
    print("output tokens: ", response.usage.output_tokens)

    data_object = json.loads(response.output_text)

    return response.output_text

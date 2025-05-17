from openai import OpenAI
import os
import json
from dotenv import load_dotenv
import base64
from constants.openAI_constants import OPENAI_ONLY_SYSTEM_PROMPT

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def analyze_image(request):
    image = request.files["image"]
    image_data = image.read()
    image_base64 = base64.b64encode(image_data).decode("utf-8")

    client = OpenAI(api_key=openai_api_key)
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

    for key in data_object:
        print(f"{key}: {data_object[key]}")

    return response.output_text

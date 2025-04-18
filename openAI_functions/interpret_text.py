from openai import OpenAI
import os
from dotenv import load_dotenv
from constants.openAI_constants import SYSTEM_PROMPT

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def interpret_text(request):
    body = request.get_json()
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "developer",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"Please interpret the following text: {body['text']}. ",
            },
        ],
        temperature=0,
    )

    result = response.choices[0].message.content

    return result

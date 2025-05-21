from openai import OpenAI
import os
from dotenv import load_dotenv
from constants.openAI_constants import SYSTEM_PROMPT
import json

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def interpret_text(textract_response):
    client = OpenAI(api_key=openai_api_key)
    json_string = json.dumps(textract_response)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "developer",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"Please interpret the following text: {json_string}. ",
            },
        ],
        temperature=0,
    )
    print("TEXTRACT + OPENAI")
    print("total tokens: ", response.usage.total_tokens)
    print("prompt tokens: ", response.usage.prompt_tokens)
    print("output tokens: ", response.usage.completion_tokens)

    result = response.choices[0].message.content

    return result

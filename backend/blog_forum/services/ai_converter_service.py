
from openai import OpenAI
import requests
#import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_URL = "https://api.x.ai"
ENDPOINT = "/v1/chat/completions"

# Need to set up how API key is retrieved
# TO DO here
#API_KEY = os.getenv("XAI_API_KEY")

API_KEY = "xai-T603mgebZ4hRWVqhAHkScrVnkCyfzwWGcdauEMiPsRCEi6lUYbyNgCdGEQ8ZnhfXMXTJiKqP6BPIMWEl"

def convert_content(content, author):
    """
    Convert the content using the AI model.
    """
    system_query = f"You can convert posts to make them sound more like {author}."
    message_query = content
    messages = [
        {
            "role": "system", "content": system_query
        },
        {
            "role": "user", "content": message_query
        },
    ]


    client = OpenAI(
        base_url = BASE_URL,
        api_key = API_KEY,
    )

    ##TODO: This format is wrong and returns a 404 from grok api need to fix
    # maybe try using a raw request to the endpoint instead of the client wrapper

    payload = {
        "model": "grok-3-mini-beta",
        "reasoning_effort": "low",
        "messages": messages,
        "temperature": 1.0,
    }
    url = f"{BASE_URL}{ENDPOINT}"
    resp= requests.post(url, json=payload, headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"})
    json_response = resp.json()
    logger.info(json_response)

    # If response successful, insert into db before returning to view
    # TO DO here

    
    return {'status': 'success', 'converted_content': json_response['choices'][0]['message']['content']}
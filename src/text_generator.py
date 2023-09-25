import yaml
import openai
from src.prompt_handler import get_messages

def get_openai_response(request):
    openai.api_key = get_openai_key()

    messages = get_messages()

    messages.append({
        "role": "user",
        "content": request 
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response

def get_openai_key():
    try:
        # Load the configuration
        with open("settings.yml", "r") as f:
            config = yaml.safe_load(f)

        key = config.get("settings", {}).get("open_ai_key", "")
        
        return key

    except (FileNotFoundError, yaml.YAMLError):
        pass
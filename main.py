from src.mod_handler import execute
from src.text_generator import get_openai_response
import json
import ast

print("Welcome to the NLP Assistant Demo Project!\n")

while True:
    try:
        request = input("What would you like for me to do?\n\n")
        response = get_openai_response(request)
        response_content = response["choices"][0]["message"]["content"]
        obj = ast.literal_eval(response_content)

        for item in obj["endpoints"]:
            execute(item)

        print(obj["response"])
    except Exception as e:
        print("There is an issue with the response.")
        print("Exception:", e)
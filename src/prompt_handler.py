from src.mod_handler import get_mods
import yaml
import os

def get_prompt_string():
    try:
        with open("settings.yml", "r") as f:
            config = yaml.safe_load(f)
        
        assistant = config.get("settings", {}).get("current_assistant_instructions")
        if not assistant:
            return ""
        
        assistant_config_path = os.path.join("assistant_instructions", f"{assistant}.yml")
        with open(assistant_config_path, "r") as f_two:
            config_two = yaml.safe_load(f_two)
        
        description = config_two.get("instructions", {}).get("description", "")
        if not description:
            return ""

        prompt_string = f"{description.strip()}\n\nCurrent API:\n\n"

        mods = get_mods()

        for mod_name, mod in mods.items():
            for endpoint_name, endpoint in mod.endpoints.items():
                params = '&'.join([f"{param_name}={param_type}" for param_name, param_type in endpoint.params.items()])
                prompt_str = f"Endpoint: {mod_name}/{endpoint_name}?{params}\nDescription: {endpoint.description.strip()}"
                prompt_string = f"{prompt_string}{prompt_str}\n\n"

        return prompt_string.strip()

    except (FileNotFoundError, yaml.YAMLError):
        return ""
    
def get_examples_list():
    examples_list = []
    try:
        # Load the configuration
        with open("settings.yml", "r") as f:
            config = yaml.safe_load(f)

        assistant = config.get("settings", {}).get("current_assistant_instructions")
        if not assistant:
            return []
        
        # Load assistant-specific configuration
        assistant_config_path = os.path.join("assistant_instructions", f"{assistant}.yml")
        with open(assistant_config_path, "r") as f_two:
            config_two = yaml.safe_load(f_two)
        
        examples = config_two.get("instructions", {}).get("examples", {})
        
        for _, value in examples.items():
            user_input = value.get("user", "").strip()
            assistant_response = value.get("assistant", "").strip()
            examples_list.append({
                "user": user_input,
                "assistant": assistant_response
            })

    except (FileNotFoundError, yaml.YAMLError):
        pass

    return examples_list
    
def get_messages():
    messages = []

    messages.append(
    {
        "role": "system",
        "content": get_prompt_string()
    })

    examples = get_examples_list()

    for example in examples:
        messages.append({
            "role": "user",
            "content": example["user"]
        })

        messages.append({
            "role": "assistant",
            "content": example["assistant"]
        })

    return messages
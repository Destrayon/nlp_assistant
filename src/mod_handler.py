import os
import importlib.util
import yaml

class Endpoint:
    def __init__(self, func, description, params):
        self.func = func
        self.description = description
        self.params = params

    def call(self, **kwargs):
        return self.func(**kwargs)


class FormattedEndpoint:
    def __init__(self, function, description):
        self.function = function
        self.description = description

    

class Mod:
    def __init__(self, path):
        self.endpoints = {}

        with open(os.path.join(path, "config.yml"), "r") as f:
            config = yaml.safe_load(f)
            if "endpoints" in config:
                for endpoint_name, details in config["endpoints"].items():
                    spec = importlib.util.spec_from_file_location("module.name", os.path.join(path, "source.py"))
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    func = getattr(module, endpoint_name)
                    self.endpoints[endpoint_name] = Endpoint(func, details.get("description", ""), details.get("parameters", {}))

    def call(self, function_name, **params):
        return self.endpoints[function_name].call(**params)

_MODS = None

def get_mods(path='mods'):
    global _MODS
    if _MODS is None:
        mods = {}
        for dir_name in os.listdir(path):
            dir_path = os.path.join(path, dir_name)
            if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, "source.py")) and os.path.exists(os.path.join(dir_path, "config.yml")):
                mods[dir_name] = Mod(dir_path)
        _MODS = mods
    return _MODS

def execute(endpoint_str):
    mods = get_mods()
    parts = endpoint_str.split('?')
    mod_name, function_name = parts[0].split('/')
    params = dict(param.split('=') for param in parts[1].split('&'))
    return mods[mod_name].call(function_name, **params)

def generate_prompt_strings(path='mods'):
    prompt_strings = []

    mods = get_mods(path)

    for mod_name, mod in mods.items():
        for endpoint_name, endpoint in mod.endpoints.items():
            params = '&'.join([f"{param_name}={param_type}" for param_name, param_type in endpoint.params.items()])
            prompt_str = f"Endpoint: {mod_name}/{endpoint_name}?{params}\nDescription: {endpoint.description.strip()}"
            prompt_strings.append(prompt_str)

    return prompt_strings
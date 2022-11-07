import json
from typing import Any


class JsonUtils:
    @staticmethod
    def load_from_file(path_to_file: str):
        with open(path_to_file, encoding="Utf-8") as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def write_to_file(path_to_file: str, data: Any):
        with open(path_to_file, "w", encoding="Utf-8") as json_file:
            json.dump(data, json_file, indent=2)

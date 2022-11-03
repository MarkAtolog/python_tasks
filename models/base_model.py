import json
from abc import ABC
from typing import Any

from utils.json_encoder import ComplexEncoder


class BaseModel(ABC):
    @classmethod
    def create_from_json_file(cls, path_to_file: str):
        with open(path_to_file, "r", encoding="Utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            model = []
            for entity in data:
                model.append(cls(**entity))
        elif isinstance(data, dict):
            model = cls(**data)
        else:
            raise NotImplementedError

        return model

    @classmethod
    def write_to_json_file(cls, path_to_file: str, data: Any):
        with open(path_to_file, "w", encoding="Utf-8") as file:
            json.dump(data, file, cls=ComplexEncoder, indent=2)

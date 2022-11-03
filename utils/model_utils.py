import json
from typing import Any

from utils.json_encoder import ComplexEncoder


class ModelUtils:
    @staticmethod
    def create_from_json_file(path_to_file: str, obj: Any):
        with open(path_to_file, "r", encoding="Utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            model = []
            for entity in data:
                model.append(ModelUtils.create_from_dict(entity, obj))
        elif isinstance(data, dict):
            model = obj(**data)
        else:
            raise NotImplementedError

        return model

    @staticmethod
    def create_from_dict(dict_to_parse: dict, obj: Any):
        return obj(**dict_to_parse)

    @staticmethod
    def write_to_json_file(path_to_file: str, data: Any):
        with open(path_to_file, "w", encoding="Utf-8") as file:
            json.dump(data, file, cls=ComplexEncoder, indent=2)

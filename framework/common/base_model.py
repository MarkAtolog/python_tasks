from typing import Any

from framework.common.json_utils import JsonUtils
from framework.common.string_utils import StringUtils


class BaseModel:
    def to_json(self):
        """
        Creates dict for object and nested objects with valid keys
        :return: a dictionary
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            valid_key = StringUtils.change_letter_case(key.strip("_")
                                                       .strip(self.__class__.__name__)
                                                       .strip("_"),
                                                       self.case)
            new_dict[valid_key] = value.to_json() if isinstance(value, BaseModel) else value
        return new_dict

    @classmethod
    def create_from_json_file(cls, path_to_file: str):
        """
        :param path_to_file: path to file containing json with data you need to parse
        :return: an object or a list of objects
        """
        data = JsonUtils.load_from_file(path_to_file)

        return cls.create_from_dict(data)

    @classmethod
    def create_from_dict(cls, data: dict | list[dict]):
        """
        :param data: data you want to parse
        :return: an object or a list of objects
        """

        return [cls(**entity) for entity in data] if isinstance(data, list) else cls(**data)

    @classmethod
    def write_to_json_file(cls, path_to_file: str, data: Any):
        JsonUtils.write_to_file(path_to_file, data.to_json())

    def __str__(self):
        return self.to_json().__str__()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.to_json() == other.to_json()

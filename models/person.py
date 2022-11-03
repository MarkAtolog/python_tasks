import json

from models.address import Address
from utils.json_encoder import ComplexEncoder


class Person:
    def __init__(self,
                 name: str,
                 surname: str,
                 age: int,
                 phone_number: list[str],
                 address: list[dict | Address]):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number
        self.address = [Address(**item) for item in address]

    def json_repr(self):
        return self.__dict__

    def to_new_file(self, file_name: str):
        with open(file_name, "w", encoding="Utf-8") as file:
            json.dump(self.__dict__, file, cls=ComplexEncoder, indent=2)

    @classmethod
    def from_string(cls, json_string: str):
        return cls.from_dict(json.loads(json_string))

    @classmethod
    def from_dict(cls, dict_to_parse: dict):
        return cls(**dict_to_parse)

    @classmethod
    def from_file(cls, path_to_file: str):
        with open(path_to_file, "r", encoding="Utf-8") as file:
            return cls.from_dict(json.load(file))

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.__class__.__qualname__ != self.__class__.__qualname__:
            raise NotImplementedError
        return self.__dict__ == other.__dict__

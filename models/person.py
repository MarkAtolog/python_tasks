import json

from models.address import Address
from models.base_model import BaseModel


class Person(BaseModel):
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

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.__class__.__qualname__ != self.__class__.__qualname__:
            raise NotImplementedError
        return self.__dict__ == other.__dict__

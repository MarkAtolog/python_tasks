from models.address import Address
from models.base_model import BaseModel


class Person(BaseModel):
    def __init__(self,
                 name: str,
                 surname: str,
                 age: int,
                 phone_number: list[str],
                 address: list[dict | Address]):
        self._name = name
        self._surname = surname
        self._age = age
        self._phone_number = phone_number
        self._address = [Address(**item) for item in address]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self._surname = surname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age

    def json_repr(self):
        new_dict = dict()
        for key in self.__dict__:
            new_dict[key.strip("_")] = self.__dict__[key]
        return new_dict

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.__class__.__qualname__ != self.__class__.__qualname__:
            raise NotImplementedError
        return self.__dict__ == other.__dict__

class Address:
    def __init__(self,
                 country: str,
                 city: str,
                 street: str,
                 house: int,
                 index: str,
                 letter: str = None):
        self.country = country
        self.city = city
        self.street = street
        self.house = house
        self.letter = letter
        self.index = index

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

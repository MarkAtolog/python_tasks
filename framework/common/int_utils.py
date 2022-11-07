from random import randint


class IntUtils:
    @staticmethod
    def random_number(start=0, stop=100):
        return randint(start, stop)

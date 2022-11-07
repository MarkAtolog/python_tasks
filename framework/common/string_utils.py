import random
from string import ascii_letters


class StringUtils:
    class Case:
        """
        Contains functions for converting string from snake case to camel case and back
        """
        snake_case = lambda self, s: str([char if char.islower() else "_" + char.lower() for char in s[1:]]).lower()
        lower_camel_case = lambda self, s: s[0].lower() + s.title().replace("_", "")[1:]
        upper_camel_case = lambda self, s: s.title().replace("_", "")

    @staticmethod
    def get_random_string(length=8):
        string = ''.join(random.choices(ascii_letters, k=length))
        return string

    @staticmethod
    def change_letter_case(string: str, case):
        """
        :param string: string you need to transform
        :param case: function from StringUtils.Case class
        :return: transformed string
        """
        return case(string)

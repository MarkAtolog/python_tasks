from framework.common.base_model import BaseModel
from framework.common.string_utils import StringUtils


class Company(BaseModel):
    case = StringUtils.Case.lower_camel_case

    def __init__(self, **fields):
        self.__name = fields.get("name")
        self.__catch_phrase = fields.get("catch_phrase") \
                                if fields.get("catchPhrase") is None \
                                else fields.get("catchPhrase")
        self.__bs = fields.get("bs")

    @property
    def name(self):
        return self.__name

    @property
    def catch_phrase(self):
        return self.__catch_phrase

    @property
    def bs(self):
        return self.__bs

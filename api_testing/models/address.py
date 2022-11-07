from api_testing.models.geo import Geo
from framework.common.base_model import BaseModel
from framework.common.string_utils import StringUtils


class Address(BaseModel):
    case = StringUtils.Case.lower_camel_case

    def __init__(self, **fields):
        self.__street = fields.get("street")
        self.__suite = fields.get("suite")
        self.__city = fields.get("city")
        self.__zipcode = fields.get("zipcode")
        self.__geo = Geo(**fields.get("geo")) \
            if isinstance(fields.get("geo"), dict) \
            else fields.get("geo")

    @property
    def street(self):
        return self.__street

    @property
    def suite(self):
        return self.__suite

    @property
    def city(self):
        return self.__city

    @property
    def zipcode(self):
        return self.__zipcode

    @property
    def geo(self):
        return self.__geo

from framework.common.base_model import BaseModel
from framework.common.string_utils import StringUtils


class Geo(BaseModel):
    case = StringUtils.Case.lower_camel_case

    def __init__(self, **fields):
        self.__lat = fields.get("lat")
        self.__lng = fields.get("lng")

    @property
    def lat(self):
        return self.__lat

    @property
    def lng(self):
        return self.__lng

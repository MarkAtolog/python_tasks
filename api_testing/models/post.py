from framework.common.base_model import BaseModel
from framework.common.string_utils import StringUtils


class Post(BaseModel):
    case = StringUtils.Case.lower_camel_case

    def __init__(self, **fields):
        self.__user_id = fields.get("user_id") if fields.get("userId") is None else fields.get("userId")
        self.__id = fields.get("id")
        self.__title = fields.get("title")
        self.__body = fields.get("body")

    @property
    def user_id(self):
        return self.__user_id

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def body(self):
        return self.__body

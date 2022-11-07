from api_testing.models.address import Address
from api_testing.models.company import Company
from framework.common.base_model import BaseModel
from framework.common.string_utils import StringUtils


class User(BaseModel):
    case = StringUtils.Case.lower_camel_case

    def __init__(self, **fields):
        self.__id = fields.get("id")
        self.__name = fields.get("name")
        self.__username = fields.get("username")
        self.__email = fields.get("email")
        self.__address = Address(**fields.get("address")) \
                            if isinstance(fields.get("address"), dict) \
                            else fields.get("address")
        self.__phone = fields.get("phone")
        self.__website = fields.get("website")
        self.__company = Company(**fields.get("company")) \
                            if isinstance(fields.get("company"), dict) \
                            else fields.get("company")

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

    @property
    def website(self):
        return self.__website

    @property
    def company(self):
        return self.__company

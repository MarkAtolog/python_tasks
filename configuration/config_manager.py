import os

from framework.common.json_utils import JsonUtils


class ConfigManager:
    __CONFIG_FILE_NAME = "config.json"
    __MODULE_PATH = os.path.dirname(__file__)
    __CONFIG_FILE_PATH = os.path.join(__MODULE_PATH, __CONFIG_FILE_NAME)

    @classmethod
    def config(cls, key):
        data = JsonUtils.load_from_file(cls.__CONFIG_FILE_PATH)
        return data[key]

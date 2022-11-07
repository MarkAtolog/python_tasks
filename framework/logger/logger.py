import logging.config
import os

from framework.common.json_utils import JsonUtils


class Logger:
    __LOGGER_CONFIG_FILE_NAME = "logger_config.json"
    __MODULE_PATH = os.path.dirname(__file__)
    __LOGGER_CONFIG_FILE_PATH = os.path.join(__MODULE_PATH, __LOGGER_CONFIG_FILE_NAME)

    def __init__(self):
        logging.config.dictConfig(JsonUtils.load_from_file(self.__LOGGER_CONFIG_FILE_PATH))
        self.logger = logging.getLogger('main_logger')

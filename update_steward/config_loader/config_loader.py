from configparser import ConfigParser


class ConfigLoader:

    def __init__(self) -> None:
        self.config_parser = ConfigParser()

    def read_config_file(self, path_to_read: str):
        self.config_parser.read(path_to_read)

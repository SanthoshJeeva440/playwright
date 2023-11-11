from jproperties import Properties


class Config_Manager:
    configs = Properties()
    with open('data/qa.properties', 'rb') as config_file:
        configs.load(config_file)

    @staticmethod
    def setup(key: str) -> str:
        return Config_Manager.configs.get(key)[0]

    @staticmethod
    def channel() -> str:
        return Config_Manager.setup("channel")

    @staticmethod
    def browser() -> str:
        return Config_Manager.setup("browser")

    @staticmethod
    def headless() -> bool:
        return bool(Config_Manager.setup("headless"))

    @staticmethod
    def url() -> str:
        return Config_Manager.setup("url")

import json

from mimeo.consumers import ConsumerFactory
from mimeo.generators import GeneratorFactory
from mimeo.config.mimeo_config import MimeoConfig


class Mimeograph:

    def __init__(self, config_path):
        self.mimeo_config = Mimeograph.__get_config(config_path)
        self.__generator = GeneratorFactory.get_generator(self.mimeo_config)
        self.__consumer = ConsumerFactory.get_consumer(self.mimeo_config)

    def produce(self):
        for data in self.__generator.generate(self.mimeo_config.templates):
            data_str = self.__generator.stringify(data, self.mimeo_config)
            self.__consumer.consume(data_str)

    @staticmethod
    def __get_config(config_path):
        with open(config_path) as config_file:
            config = json.load(config_file)
        return MimeoConfig(config)

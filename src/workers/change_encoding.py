from utils import logger_util

class ChangeEncoding:

    def __init__(self, logger):
        self.logger = logger_util.create_logger(logger_name)

    def run(self, data):
        # main function of a worker
        self.logger.info('Changing encoding ...')
        self.logger.debug('Encoding is ' + data['encoding'])

        self.logger.info('Finishes encoding')

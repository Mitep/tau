from utils.logger_utils import create_logger


class ApplyState:

    def __init__(self, logger_name):

        self.logger = create_logger(logger_name)
        self.logger.info("Apply state worker initialized.")

    def run(self, data):

        self.logger.info('Applying state ...')

        # applying

        self.logger.info('Applying finished.')

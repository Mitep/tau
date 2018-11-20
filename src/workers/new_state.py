from utils.logger_utils import create_logger


class NewState:
    
    def __init__(self, logger_name):
        self.logger = create_logger(logger_name)
        self.logger.info("New state worker initialized.")

    def run(self, data):
        
        self.logger.info('Calculating new state ...')

        # calculating

        self.logger.info('Calculating new state finished')


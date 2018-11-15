from utils import logger_util

class CurrentState:
    
    def __init__(self, logger_name):
        self.logger = logger_util.create_logger(logger_name)
    
    def run(self, data):
        # main function of a worker
        self.logger.info('Calculating current state ...')
        self.logger.debug('Finding files in directory ' + data['dir_path'])
        self.logger.debug('Saving current state of dir into a ' + data['state_path'])

        self.logger.info('Calculating current state finished')


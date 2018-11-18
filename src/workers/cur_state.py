from utils import logger_util
from utils import mu_dir

class CurrentState:
    

    def __init__(self, logger_name):
        self.logger = logger_util.create_logger(logger_name)
    

    def run(self, data):
        # main function of a worker
        self.logger.info('Calculating current state ...')

        music_dir = data['MUSIC_DIR']
        self.logger.debug(music_dir)

        mu_files, mu_dirs = mu_dir.get_dir_files(music_dir)

        self.logger.debug("Print dirs:")
        for dir in mu_dirs:
            self.logger.debug(dir)

        self.logger.info('Calculating current state finished')


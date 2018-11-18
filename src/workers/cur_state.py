import os
from utils import logger_util
from utils import tags_util


class CurrentState:
    

    def __init__(self, logger_name):
        self.logger = logger_util.create_logger(logger_name)
    

    def run(self, data):
        # main function of a worker
        self.logger.info('Calculating current state ...')

        music_dir = data['MUSIC_DIR']
        self.logger.debug(music_dir)

        for root, dirs, files in os.walk(music_dir, topdown=True):
            for name in files:
                print(os.path.join(root, name))
                print(tags_util.get_tags(os.path.join(root, name)))
                #print(type(tags_util.get_tags(os.path.join(root, name))))
            '''
            for name in dirs:
                print(os.path.join(root, name))
            '''

        self.logger.info('Calculating current state finished')


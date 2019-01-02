from utils.logger_utils import create_logger
from utils.file_utils import filter_ext
from utils.file_utils import get_files
from utils.state_utils import save_state
from utils.state_utils import add_timestamp
from utils.state_utils import get_state_file


class CurrentState:

    def __init__(self, logger_name):

        self.logger = create_logger(logger_name)
        self.logger.info("Current state worker initialized.")

    def run(self, data):

        self.logger.info('Printing current state ...')
        self.logger.info("Config for printing state:")

        root_dir = data['ROOT']
        print_cfg = data['PRINT_CFG']
        state_dir = data['STATE_DIR']

        self.logger.info("Root dir: " + root_dir)

        for conf in print_cfg:
            self.logger.info(conf + ":" + str(print_cfg[conf]))

        self.logger.info("Start printing...")

        music_files = filter_ext(['mp3'])(get_files)(root_dir)

        state_filepath = get_state_file(state_dir)
        add_timestamp(state_filepath)

        for music_file in music_files:

            song = {}
            song['filepath'] = music_file

            song['a'] = 'g'
            song['b'] = 'h'
            song['c'] = 'j'
            # add metadata to song

            save_state(song, state_filepath)

        self.logger.info('Printing current state finished.')

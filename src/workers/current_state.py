from utils.logger_utils import create_logger
from utils.file_utils import *
from utils.state_utils import save_state
import utils.state_tree as tree


class CurrentState:
    
    def __init__(self, logger_name):
        self.logger = create_logger(logger_name)
        self.logger.info("Current state worker initialized.")

    def run(self, data):
        
        self.logger.info('Printing current state ...')
        self.logger.info("Config for printing state:")
        
        root_dir = data['ROOT']
        state_dir = data['STATE_DIR']
        print_cfg = data['PRINT_CFG']

        self.logger.info("Root dir: " + root_dir)

        for conf in print_cfg:
            self.logger.info(conf + ":" + str(print_cfg[conf]))

        self.logger.info("Start printing...")
        
        music_files = filter_ext(['mp3'])(get_files)(root_dir)

        current_state = []
        
        for music_file in music_files:
            
            song = tree.AudioFile(music_file)
            
            # add metadata to song

            current_state.append(song)

        save_state(current_state, state_dir)

        self.logger.info('Printing current state finished.')


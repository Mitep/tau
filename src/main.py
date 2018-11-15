import sys
import os
from workers.cur_state import CurrentState
from workers.change_encoding import ChangeEncoding
from utils import logger_util
from utils import conf_utils


def start_worker(worker_type, config_file):
    
    logger = logger_util.create_logger('main_logger')
    logger.info('Starting TAU ...')

    data = conf_utils.conf_dict(config_file)
    logger.debug(data)

    worker = None
    if worker_type == 'current_state':
        worker = CurrentState('calc_cur_state')
        logger.info('Starting calculate current state worker')
    elif worker_type == 'change_encoding':
        worker = ChangeEncoding('encoder')
        logger.info('Starting encoding worker')
    else:
        logger.warning('No worker type ' + worker_type)
        return

    worker.run(data)
    

if __name__ == '__main__':
    start_worker('current_state', './config/config.yaml')
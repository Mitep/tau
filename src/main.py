import sys
import os
from workers.cur_state import CurrentState
from workers.change_encoding import ChangeEncoding
from utils import logger_util
from utils import arg_data

def start_worker(worker_type, config):
    logger = logger_util.create_logger('main_logger')
    logger.info('Starting TAU ...')

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

    data = arg_data.get_data(config)
    worker.run(data)

if __name__ == '__main__':
    start_worker('current_state', 'data_path')
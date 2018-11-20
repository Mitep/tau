from workers.current_state import CurrentState
from workers.new_state import NewState
from workers.apply_state import ApplyState
from utils.config_utils import load_config
from utils.logger_utils import create_logger


logger = create_logger('main_logger')

def start_worker(worker_type, config_path):

    logger.info("Starting TAU ...")

    config_data = load_config(config_path)

    worker = None
    if worker_type == 'current_state':
        worker = CurrentState(worker_type)
    elif worker_type == 'new_state':
        worker = NewState(worker_type)
    elif worker_type == 'apply_state':
        worker = ApplyState(worker_type)
    else:
        logger.warning('No worker type ' + worker_type)
        return

    worker.run(config_data)


if __name__ == '__main__':
    start_worker('current_state', './config/config.yaml')

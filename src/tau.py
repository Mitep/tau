import click

from workers.current_state import CurrentState
from workers.new_state import NewState
from workers.apply_state import ApplyState
from utils.config_utils import load_config
from utils.logger_utils import create_logger


logger = create_logger('tau_logger')


@click.command()
@click.option(
    '--worker',
    default='current',
    help='Worker type. Possible types: current[default], new, apply.')
@click.option(
    '--config',
    default='./config/config.yaml',
    help='Config file. If not set it will be loaded default config.')
def start_worker(worker, config):

    config_data, msg = load_config(config)

    if config_data is None:
        logger.error(msg)
        return

    logger.info(msg)

    running_worker = None

    if worker == 'current':
        running_worker = CurrentState(worker)

    elif worker == 'new':
        running_worker = NewState(worker)

    elif worker == 'apply':
        running_worker = ApplyState(worker)

    else:
        logger.error('No worker type ' + type)
        return

    logger.info(f'Starting worker for {worker} state.')

    running_worker.run(config_data)


if __name__ == '__main__':

    logger.info('Starting TAU ...')

    start_worker()

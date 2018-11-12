from workers.cur_state import CurrentState
from utils import logger_util

logger = logger_util.create_logger('main_logger')
logger.info('main logger')

data = {}
data['dir_path'] = 'path to music dir'
data['state_path'] = 'path where state yaml file will be created'

current = CurrentState('current_state_logger')
current.run(data)

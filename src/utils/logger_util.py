import logging

def create_logger(logger_name):

    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger

if __name__ == '__main__':
    logger = create_logger('logger_util')
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    #logger.warn('warn message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

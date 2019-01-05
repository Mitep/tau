"""
Common utils used all around
"""

import os
import logging
import datetime
import yaml


def date():
    now = datetime.datetime.now()
    return f"{now.day}_{now.month}_{now.year}"


def time():
    now = datetime.datetime.now()
    return f"{now.hour}_{now.minute}_{now.second}"


def config(filepath):
    with open(filepath, "r") as f:
        return yaml.load(f)


class Logger:

    loggers = {}

    def get(name):
        if name in Logger.loggers.keys():
            return Logger.loggers[name]
        else:
            logger = Logger(name)
            Logger.loggers[name] = logger
            return logger

    def __init__(self, name):
        self.console = self.cl(name)
        self.file = self.fl(name)

    def info(self, msg):
        self.console.info(msg)
        self.file.info(msg)

    def debug(self, msg):
        self.console.debug(msg)
        self.file.debug(msg)

    def warning(self, msg):
        self.console.warning(msg)
        self.file.warning(msg)

    def error(self, msg):
        self.console.error(msg)
        self.file.error(msg)

    def cl(self, name):
        logger = logging.getLogger(f"{name}_cl")
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(levelname)s - %(message)s")
        ch.setFormatter(formatter)

        logger.addHandler(ch)

        return logger

    def fl(self, name):

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        log_dir = f"{os.getcwd()}{os.sep}log"

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        fh = logging.FileHandler(f"{log_dir}{os.sep}{date()}_{name}.log")
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        fh.setFormatter(formatter)

        logger.addHandler(fh)

        return logger


def list_dir(path):
    tuple_list = []
    for root, dirs, files in os.walk(path, topdown=True):
        root = root[len(path):]
        for name in files:
            tuple_list.append(tuple(os.path.join(root, name).split(os.sep)))
        for name in dirs:
            tuple_list.append(tuple(os.path.join(root, name).split(os.sep)))

    return tuple_list


def is_dir(path):
    if path[-1].find(".") <= 0:
        return True
    return False

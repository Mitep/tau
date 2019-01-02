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


def logger(name):
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers:
        return logger

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    log_dir = f"{os.getcwd()}{os.sep}log"
    print(log_dir)
    try:
        os.makedirs(log_dir)
    except OSError:
        print(f"Log dir exist.")

    # create file handler which logs even debug messages
    fh = logging.FileHandler(f"{log_dir}{os.sep}{date()}{name}.log")
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
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

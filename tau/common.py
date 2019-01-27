"""
Common utils used all around app
"""

import os
import datetime
import logging


def date():
    """
    Return current date in d_m_y format
    Used in logger when creating log file
    """
    now = datetime.datetime.now()
    return f"{now.day}_{now.month}_{now.year}"


def time():
    """
    Retun current time in h_m_s format
    """
    now = datetime.datetime.now()
    return f"{now.hour}_{now.minute}_{now.second}"


class Logger:
    """
    Logger class
    """

    logger = None

    def get():
        if Logger.logger is None:
            Logger.logger = logging.getLogger("tau")
            Logger.logger.setLevel(logging.DEBUG)

            # console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            logDir = f"{os.getcwd()}{os.sep}log"

            if not os.path.exists(logDir):
                os.makedirs(logDir)

            # file handler
            fh = logging.FileHandler(f"{logDir}{os.sep}log_{date()}.log")
            fh.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )

            ch.setFormatter(formatter)
            fh.setFormatter(formatter)

            Logger.logger.addHandler(ch)
            Logger.logger.addHandler(fh)

        return Logger.logger

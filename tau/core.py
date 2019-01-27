"""
Tau core functionalities
"""

import common
# import extra


def run(service, params):
    """
    Function that starts core and extra services
    """

    logger = common.Logger.get()

    # if service was found
    logger.info("Running service {service} with {params} params")


def help():
    """
    Prints help in terminal
    """

    # load help from file and print in terminal
    print("help")

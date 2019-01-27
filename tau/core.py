"""
Tau core functionalities
"""

import common


def run(service, params):
    """
    Function that starts core services
    """

    logger = common.Logger.get()

    # if service was found
    logger.info("Running service {service} with {params} params")

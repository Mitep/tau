"""
Main module
Used for arg parsing and calling tau services
"""

import sys

import common
# import core
# import extra


def runner(params):
    """
    Run services based on given parameters
    """

    logger = common.Logger.get()

    logger.info("Running service")
    logger.info(f"Input parameters: {params}")


def main():
    """
    Main function
    Getting user args and starting tau services
    """

    logger = common.Logger.get()

    logger.info("Starting tau")

    args = sys.argv[1:]

    try:
        while True:
            runner(args)
    except KeyboardInterrupt:
        logger.info("Exiting tau...")


if __name__ == "__main__":

    main()

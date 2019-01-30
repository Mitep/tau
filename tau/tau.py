"""
Main module
Used for arg parsing and calling tau services
"""

import sys

import common
import services


def runner(args):
    """
    Run services based on given arguments
    """

    logger = common.Logger.get()

    logger.info("Parsing arguments: {args}")

    # this should be parsed from config file and cli args
    cfgDict = {"namae": "John", "age": "23"}

    # read from config or command line which service to call
    # this is just test to see if services are working
    
    funToRun = getattr(services, "testService")
    funToRun(cfgDict)
    # services.service.registered["testService2"](cfgDict)


def main():
    """
    Main function
    Getting user args and starting tau services
    """

    logger = common.Logger.get()

    logger.info("Starting tau")

    try:
        runner(sys.argv[1:])
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt")

    logger.info("Exiting tau...")


if __name__ == "__main__":

    main()

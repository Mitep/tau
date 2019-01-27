"""
Main module
Used for arg parsing and calling tau services
"""

import sys

import common
import core


def argParser(args):
    """
    Creating dict out of given args from command line
    """

    argDict = {}

    for i, x in enumerate(args):
        if x[0:1] == "-" and i < len(args):
            argDict[x[1:]] = args[i + 1]
        if x.startswith("--"):
            key, val = x[2:].split("=", 1)
            argDict[key] = val

    return argDict


def runner(params):
    """
    Run services based on given parameters
    """

    logger = common.Logger.get()

    logger.info("Running service")
    logger.info(f"Input parameters: {params}")

    if "help" in params.keys():
        core.help()
        return

    if "start" not in params.keys():
        logger.error(
            "start param not found.",
            "tau must know which service to start",
            "exiting...")
        raise AttributeError

    # if start was something like
    # encode->edit->estimate
    # then it runs service one by one
    services = params["start"].split("->")

    del services["start"]

    for service in services:
        core.run(service, params)


def main():
    """
    Main function
    Getting user args and starting tau services
    """

    logger = common.Logger.get()

    logger.info("Starting tau")

    params = argParser(sys.argv[1:])

    try:
        while True:
            runner(params)
    except KeyboardInterrupt:
        logger.info("Exiting tau...")
    except AttributeError:
        logger.info("Exiting tau...")


if __name__ == "__main__":

    main()

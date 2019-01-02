import sys

import core
import utils
import cli


def flow(flow_path):
    print("running flow")


def tau():

    logger = utils.Logger.get("tau")

    cli.welcome()

    if len(sys.argv) > 1:
        flow(sys.argv[1])
        return

    functions = core.Functions()

    try:
        while True:
            work = cli.choose_work()

            if work >= 0 and work <= 4:
                functions.functions[work]()
            else:
                logger.error(f"Tau does'n contain {work} function.")
    except KeyboardInterrupt:
        logger.info("Exiting Tau...")


if __name__ == "__main__":

    tau()

import utils
import services as serv
import cli as cli_util


def tau():

    logger = utils.Logger.get("tau")
    logger.info("Starting TAU...")

    cli = cli_util.CLI()
    cli.welcome()

    services = serv.Services()

    try:
        while True:

            service = cli.choose()

            if service >= 0:
                logger.info(f"Running {service} service")
                services.run(service)
            else:
                logger.info("Exiting tau...")
                return
    except KeyboardInterrupt:
        logger.info("Exiting Tau...")


if __name__ == "__main__":

    tau()

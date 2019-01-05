import utils
import config as cfg


class CLI:

    def __init__(self):
        self.logger = utils.Logger.get(__name__)

    def welcome(self):
        self.logger.console.info(
            "Welcome to TAU - Helper for formatting music directory " +
            "and metadata on your PC."
        )

    def choose(self):

        self.logger.info("...Choosing service...")

        self.logger.console.info("Select service:")
        service_list = [f"[{i+1}] - {x}" for i, x in enumerate(cfg.services)]
        [self.logger.console.info(s) for s in service_list]
        self.logger.console.info("[0] - exit")

        sel_input = input("Choose: ")

        try:
            selected = int(sel_input)

            if selected > len(service_list):
                raise OverflowError

            return selected - 1
        except ValueError:
            self.logger.error(f"You choosed {selected}")
            self.logger.console.error("Error - Input was not number!!!")
            self.choose()
        except OverflowError:
            self.logger.info("Number doesn't match with any service.")
            self.choose()

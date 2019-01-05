import utils
import config as cfg
import cli
import core
import utils_estimate
import api


class Services:

    def __init__(self):

        self.logger = utils.Logger.get(__name__)
        self.functions = {
            0: self.scan,
            1: self.estimate,
            2: self.update,
            3: self.flow
        }

    def run(self, service):
        self.functions[service]()

    def scan(self):
        self.logger.info("Scaning started...")
        # self.logger.debug(f"Music dir path: {.root_path}")
        # files = utils.list_dir(config.root_path)
        # root_node = node_tree(files)

    def estimate(self):
        self.logger.info("Estimation started...")

    def update(self):
        self.logger.info("Update started...")

    def flow(self):
        self.logger.info("Runnig flow...")

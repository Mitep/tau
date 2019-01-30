
class service(object):
    """
    Register function as service
    when running some service, program first lookup name of given service
    in services list
    """

    registered = []

    def __call__(self, f):
        service.registered.append(f.__name__)
        return f


class requires(object):
    """
    When calling service if we doesn't supply it with required parameters
    This function will stop the execution
    """

    def __init__(self, *keys):
        self.keys = keys

    def __call__(self, f):

        def wrapper(cfg):

            for x in self.keys:
                if x not in cfg.keys():
                    print(f"ERROR - missing {x} in {f.__name__} service")
                    print("Returning from function...")
                    return

            f(cfg)

        return wrapper

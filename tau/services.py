from decorators import service
from decorators import requires


@requires("age")
@service()
def testService(cfg):
    print("This is test service that requires age")
    print(f"{cfg}")
    testService2(cfg)
    print("Exiting service")


@requires("name")
@service()
def testService2(cfg):
    print("This is test service2 that requres name")
    print(f"{cfg}")
    print("Exiting service")

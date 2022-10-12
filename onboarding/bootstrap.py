import os

from chocs_middleware.trace import Logger
from kink import di


def bootstrap_di() -> None:
    di["log"] = Logger.get(name=__name__, level=os.getenv("LOG_LEVEL", "ERROR"))

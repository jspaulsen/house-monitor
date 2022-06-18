import logging
from sys import stdout

from app import config


def setup_logging() -> logging.Logger:
    formatter = logging.Formatter("%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")

    handler = logging.StreamHandler(stdout)
    handler.setFormatter(formatter)

    ret = logging.getLogger()
    ret.setLevel(config.LOG_LEVEL)
    ret.addHandler(handler)

    return ret

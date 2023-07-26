import logging
from logging.handlers import TimedRotatingFileHandler

logger = None


def Logs():
    global logger

    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        file_handler = TimedRotatingFileHandler(filename='./archivo.log', when='D', interval=30, backupCount=2)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger




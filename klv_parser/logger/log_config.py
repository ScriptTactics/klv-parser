#
# Copyright SCRIPT TACTICS LLC
#
import logging
import os
from logging.handlers import RotatingFileHandler

LOGGER_MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

LOG_FMT_STR = "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - line %(lineno)d %(message)s"


def setup_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a stream handler for console output
    stream_handler = logging.StreamHandler()

    # Create a rotating file handler
    rotating_handler = RotatingFileHandler(
        f"{log_dir}/klvpy",
        maxBytes=LOGGER_MAX_BYTES,
        backupCount=BACKUP_COUNT,
    )  # Log file will rotate after 5MB, keeping 3 backups

    # Create a formatter for the log messages
    formatter = logging.Formatter(LOG_FMT_STR)

    # Apply the formatter to both handlers
    stream_handler.setFormatter(formatter)
    rotating_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(rotating_handler)

    return logger


# Setup the global logger
logger = setup_logger()

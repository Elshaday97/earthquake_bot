import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def log_info(info):
    logger.info(f"INFO: {info}")

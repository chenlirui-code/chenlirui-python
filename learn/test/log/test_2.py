from utils.log.my_logger import logger

logger.configure_logging(True, "INFO")

def test_logging():
    logger.debug("debug test_logging 信息")
    return logger.info("info test_logging 信息")

from learn.test.log.test_2 import test_logging
from utils.log.my_logger import logger

# 使用默认配置进行测试
logger.info("info quotes.py 信息")
logger.debug("debug quotes.py 信息")

test_logging()

logger.debug("debug quotes.py 后信息")

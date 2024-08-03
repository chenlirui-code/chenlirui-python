from learn.test.log.test_2 import test_logging
from utils.log.my_logger import logger

# 使用默认配置进行测试
logger.info("info test.py 信息")
logger.debug("debug test.py 信息")

test_logging()

logger.debug("debug test.py 后信息")

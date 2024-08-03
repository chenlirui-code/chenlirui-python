import logging
import os
import sys

# 获取控制台运行文件的目录（即与运行文件同一级的文件夹）
if getattr(sys, 'frozen', False):
    # 如果是可执行文件（.exe）运行时
    current_dir = os.path.dirname(sys.executable)
else:
    # 脚本运行时
    current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

# 获取当前脚本的名称（不包含扩展名）
script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]


class MyLogger:
    def __init__(self):
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)
        self._configured = False
        self.configure_logging()  # 默认配置

    def configure_logging(self, *args):
        """
        根据传入的参数来配置日志记录器
        参数:
        args: 可以是一个（自动判断类型，应为布尔类型或字符串类型）或两个参数（第一个必须是布尔类型，第二个必须是字符串类型）
        """
        # 默认配置
        log_level_str = 'INFO'
        create_file = False

        if len(args) == 1:
            param = args[0]
            if isinstance(param, bool):
                create_file = param
            elif isinstance(param, str):
                log_level_str = param
            else:
                raise TypeError("传入的单个参数类型不正确，应为布尔类型或字符串类型")
        elif len(args) == 2:
            if isinstance(args[0], bool) and isinstance(args[1], str):
                create_file = args[0]
                log_level_str = args[1]
            else:
                raise TypeError("传入的两个参数，第一个必须是布尔类型，第二个必须是字符串类型")
        elif len(args) > 2:
            raise TypeError("参数数量不正确，应为 1 个或 2 个")

        log_level = getattr(logging, log_level_str.upper(), logging.INFO)
        self.logger.setLevel(log_level)

        # 初始化 formatter 变量
        formatter = logging.Formatter('%(levelname)s:%(name)s: %(message)s')

        # 构建日志文件名
        level = logging.getLevelName(log_level).lower()
        log_file_name = f"{script_name}_{level}_log.log"
        file_path = os.path.join(current_dir, log_file_name)

        # 清除已有的处理器
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        if create_file:
            # 创建一个文件处理器
            file_handler = logging.FileHandler(file_path)
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        # 创建一个流处理器
        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        self._configured = True

    def __getattr__(self, name):
        return getattr(self.logger, name)


# 在模块加载时自动创建对象
logger = MyLogger()

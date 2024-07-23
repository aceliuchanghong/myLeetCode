"""
装饰器模式
"""

import time
import functools
import logging
from functools import lru_cache, wraps
from typing import Callable, Optional

# 设置日志器，可以记录到文件或控制台
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def log_time2(
        repeats: int = 1,
        use_cache: bool = False,
        log_level: int = logging.INFO,
        log_to: Optional[str] = None,
        logger_name: str = 'decorator_logger'
):
    def decorator(func: Callable) -> Callable:
        if use_cache:
            func = lru_cache(None)(func)  # cache the function

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = None
            total_time = 0
            for _ in range(repeats):
                result = func(*args, **kwargs)
                total_time += time.time() - start_time
                start_time = time.time()

            average_time = total_time / repeats

            # Create logger if the target is not console
            if log_to:
                logger = logging.getLogger(logger_name)
                handler = logging.FileHandler(log_to)
                handler.setLevel(log_level)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                handler.setFormatter(formatter)
                logger.addHandler(handler)
            else:
                # If logging to console, use the default logger
                logger = logging.getLogger(__name__)

            # Log the info
            logger.log(log_level, f"{func.__name__} took {average_time:.4f} seconds to run (average).")

            return result

        return wrapper

    return decorator


@log_time2(repeats=5, use_cache=False, log_level=logging.DEBUG)
def greet2(name):
    time.sleep(1)
    return f"Hello, {name}"


def add_greeting(greeting):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"{greeting} " + func(*args, **kwargs)

        return wrapper

    return decorator


@add_greeting("Hi there,")
def greet3(name):
    return f"{name}"


def log_time(func):
    # 定义一个内部函数，这个函数将包装原始函数
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 执行原始函数
        end_time = time.time()  # 记录结束时间
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result

    # 返回包装后的函数
    return wrapper


@log_time
def greet(name):
    time.sleep(1)
    return f"Hello, {name}"


if __name__ == "__main__":
    print(greet3("World"))

import logging

# DEBUG | 最详细的日志信息，典型应用场景是 问题诊断
# INFO | 信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
# WARNING | 当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
# ERROR | 由于一个更严重的问题导致某些功能不能正常运行时记录的信息
# CRITICAL | 当发生严重错误，导致应用程序不能继续运行时记录的信息

logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

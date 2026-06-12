import logger

logger.info("App started")

logger.warning("Low disk space: 2GB remaining")

logger.error("Database connection failed")

logger.debug("Retrying connection...")


print("\nERROR LOGS:")
logs = logger.read_logs(level_filter="ERROR")
print(logs)
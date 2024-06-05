# DEBUG
# INFO
# WARNING - python's security level
# ERROR
# CRITICAL

import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("You have got 20 mails in your inbox!")
logging.critical("All components failed!")

logger = logging.getLogger("my logger")
logger.info("The best logger out there")
logger.critical("Your app is down")
logger.log(logging.ERROR, "An error occurred!")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("11_mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.debug("This is a debug message!")
logger.info("This is important information!")


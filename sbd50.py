#logging
import logging

logging.basicConfig(level=logging.INFO)

logging.info("you have got 20 mails in your inbox!")
logging.critical("All components failed!")

logger = logging.getLogger("NeuralNine Logger")
logger.info("The best logger was just created!")
logger.critical("Your Youtube channel was deleted")
"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("Weather - Processing weather message")
        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        #
        try:
            msg = message.value()
            self.temperature = msg['temperature']
            self.status = msg['status']
        except Exception as e:
            logger.error(e)
        

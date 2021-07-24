import logging

logger = logging

logger.basicConfig(filename='userRegistration.log',level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger.basicConfig(filename='userRegistration.log',level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d')
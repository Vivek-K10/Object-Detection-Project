from signlanguage.logger import logging
from signlanguage.exception import SignException
import sys
#logging.info("Welcome to the project")
try:
    a= 7/'9'
except Exception as e:
    raise SignException(e,sys) from e

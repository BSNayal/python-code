from . import logger
from src.constants.constants import UNIVERSE, KINGDOMS
from .eliza import Eliza


def _initialize_logger():
    '''This function initializes the logger to log all the input/ouput
        messages and the application logs(warnings, errors etc..)
    '''
    logger.initialize()


def start(universe = None,kingdoms = None):
    ''' This function is where we start initializing the universe and
        the kingdoms. After that we start the chat console.
    parameters:
        universe: If user has defined the universe name in the input file
                    then we take that value else the default value is None
        kingdoms: If user has defined the kingdoms in the input file then we
                    take that value else the default value is None.
    '''
    _initialize_logger()

    if not universe or not kingdoms: # default universe(Southeros)
        Eliza.start_chat(universe = UNIVERSE, kingdoms = KINGDOMS)
    else:
        Eliza.start_chat(universe = universe, kingdoms = kingdoms)
        

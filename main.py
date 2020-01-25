import argparse
import json

from src.utils import starter
from src.messages.messages import MISMATCH_ERROR_MSG, MISSING_ERROR_MSG
from src.constants.constants import TOTAL_KINGDOM_PROPERTIES

def main(**kwargs):
    universe = None
    kingdoms = None
    if kwargs.get('f'):
        file_name = kwargs['f']
        data = {}
        #read the input file to get details of the universe and kingdom
        with open (file_name) as json_file:
            data = json.load(json_file)
        universe = data.get('universe')
        kingdoms= data.get('kingdoms')
        if not universe:
            raise Exception(MISSING_ERROR_MSG.format('name','universe'))
        elif not kingdoms:
            raise Exception(MISSING_ERROR_MSG.format('details','kingdoms'))
        for value in kingdoms:
            if not value.get('name'):
                raise Exception(MISSING_ERROR_MSG.format('name','kingdom'))
            elif not value.get('king'):
                raise Exception(MISSING_ERROR_MSG.format('king','kingdom'))
            elif not value.get('emblem'):
                raise Exception(MISSING_ERROR_MSG.format('emblem','kingdom')) 

    starter.start(universe = universe, kingdoms = kingdoms)


if __name__ == '__main__':
    '''The user can give the name of the universe, the kingdoms and their
        emblems from command line. These are optional arguments, if not given
        then default universe of Southeros and the default kingdoms would be
        created
    '''
    parser = argparse.ArgumentParser(prog='A Golden Crown',description='This application \
                help us to elect a king for the specified Universe')
    parser.add_argument('-f','-F', help='Name of the json file \
                        containing the details of the unvierse and the \
                        kingdoms')

    args = vars(parser.parse_args())
    main(f = args['f'])

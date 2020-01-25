import logging
import os
import sys
import re
import textwrap # to show multiple lines in the centre of the screen
import shutil # to get the console's size in columns and lines
from collections import Counter

from src.constants.constants import APP_LOGGER_NAME, CHAT_LOGGER_NAME,\
    WELCOME_MSG_WIDTH,LOG_MSG_WIDTH, Q_MARK,QUESTION_RULER, QUESTION_ALLIES,\
    KING_WORD,COLON_MARK,COMMA,FROM
from ..messages.messages import WELCOME_MSG, CHAT_LOG_MSG, APP_LOG_MSG,\
    START_MSG,ASK_RIGHT_Q_MSG,PROVIDE_RIGHT_INPUT,SENDER_NOT_FOUND,\
    SAME_SENDER_RECIEVER,CURRENT_UNIVERSE

chat_logger = logging.getLogger(CHAT_LOGGER_NAME)
app_logger = logging.getLogger(APP_LOGGER_NAME)

class Eliza(object):
    ''' I have used the name Eliza because this 
        https://en.wikipedia.org/wiki/ELIZA was my first communication channel
        with a machine :)
    '''
    _potential_king = None
    _potential_allies = []
    _allies = []
    _ruler = None
    @classmethod
    def start_chat(cls,universe, kingdoms):
        ''' This function is the heart of the application. Here the magic 
            happens :)  , so here we make the console look user friendy and
            ask user to start typing is questions as well as his inputs
        '''
        os.system('cls || clear') # clearing the console
        col = shutil.get_terminal_size()[0]
        welcome_info_lines = (textwrap.TextWrapper(WELCOME_MSG_WIDTH)).\
                                wrap(WELCOME_MSG.format(universe_name = \
                                    universe))
        chat_logger.info('*'*col)
        for line in welcome_info_lines:
            chat_logger.info(line.center(col))
            chat_logger.info('\n')
        
        #call log file info for chat logger
        cls.__log_file_info(logger = chat_logger,columns = col, \
                            msg = CHAT_LOG_MSG)

        # call log file info for app logger
        cls.__log_file_info(logger = app_logger,columns = col, \
                            msg = APP_LOG_MSG)
        universe_name = 'UNIVERSE: {}'.format(universe)
        chat_logger.info(universe_name.center(col))
        kingdom_list = []
        for kingdom in kingdoms:
            kingdom_list.append(kingdom['name']+ '( emblem = ' + \
                                kingdom['emblem'] + ', king = ' + \
                                kingdom['king'] + ')')
        chat_logger.info('KINGDOMS: {}'.format(kingdom_list).center(col))
        chat_logger.info('*'*col)
        chat_logger.info(START_MSG)
        cls.__get_input(universe = universe, kingdoms=kingdoms)
        
    
    @staticmethod
    def __log_file_info(logger, columns, msg):
        imp = '-'* (columns)
        logger.info(imp.center(columns))
        if msg == APP_LOG_MSG:
            print(imp.center(columns))
        # lets get the name and location of the log file 
        log_path = logger.handlers[0].baseFilename
        # following regular expression searches for the complete path till the 
        # last '/' or '\'
        match = re.search(r'^(.*[\\\/])', log_path) 
        if match:
            file_path = match.group()
            file_name = log_path[match.span()[1]:]
            info_lines = msg.format(filename=file_name, 
                                                file_location = file_path)
            info_lines = (textwrap.TextWrapper(LOG_MSG_WIDTH)).\
                            wrap(info_lines)
            for line in info_lines:
                logger.info(line.center(columns))
                #logger.info('\n')
                if msg == APP_LOG_MSG:
                    print(line.center(columns))
                    #print('\n')
        logger.info(imp.center(columns))
        if msg == APP_LOG_MSG:
            print(imp.center(columns))
    

    @classmethod
    def __get_input(cls,universe, kingdoms):
        '''This function waits for the user to input data'''
        data = input()
        chat_logger.removeHandler(chat_logger.handlers[1])
        chat_logger.info(data)
        chat_logger.addHandler(logging.StreamHandler(sys.stdout))
        data=data.lower()
        data = data.strip()
        if data == 'q' or data == 'quit':
            sys.exit(0)
        else:
            cls.__parse_input(data=data,universe = universe, kingdoms=kingdoms)
        cls.__get_input(universe=universe, kingdoms=kingdoms)
    

    @classmethod
    def __parse_input(cls, data,universe, kingdoms):
        if data.endswith(Q_MARK):
            cls.__parse_question(data=data,universe=universe,\
                                    kingdoms = kingdoms)
            cls.__get_input(universe=universe,kingdoms=kingdoms)
        else:
            cls.__parse_other_data(data=data,kingdoms=kingdoms,\
                                    universe=universe)
    
    
    @classmethod
    def __parse_question(cls,data,universe,kingdoms):
        ''' This function helps us to find out if the question asked relates to
            'finding the ruler of the universe' or 'finding the allies of the 
            'ruler'
        '''
        cls._potential_king = None
        q1_found = False
        q2_found = False
        #check if question relates to 'finding ruler of the universe'
        for word in QUESTION_RULER:
            if re.search(word,data):
                q1_found = True
                break

        #check if question relates to 'finding allies of the ruler'
        for word in QUESTION_ALLIES:
            if re.search(word,data):
                q2_found = True
                break

        if q1_found and q2_found:
            chat_logger.info('Output: ' + ','.join(cls._allies) if cls._allies \
                                else 'None')
        elif q1_found:
            # if user doesn't give the correct universe name
            if not re.search(universe.lower(),data):
                q1_found = False
                chat_logger.info(CURRENT_UNIVERSE.format(\
                                    name= universe))
                cls.__get_input(kingdoms=kingdoms,universe=universe)
            chat_logger.info('Output: ' + 'King ' + cls._ruler if cls._ruler \
                            else 'None')
        elif q2_found:
            chat_logger.info('Output: ' + ','.join(cls._allies) if cls._allies \
                                else 'None')
        else:
            chat_logger.info(ASK_RIGHT_Q_MSG + '\n')    
    

    @classmethod
    def __parse_other_data(cls,data,kingdoms,universe):
        '''This function parses all the inputs except questions
            parameters:
                data: input entered by user
                kingdoms: list of objects of all the kingdoms
                universe: Universe which contains all the kingdoms
        '''
        data = data.strip(' ')
        #check if the input contains sender information or recipient information
        if re.search('\\b' + FROM + '\\b',data):
            data_list = data.split()
            sender = data_list[data_list.index(FROM) + 1]
            if sender == KING_WORD:
                king = data_list[data_list.index(sender)+1]
            else:
                king = data_list[data_list.index(sender)]
            if king[-1] == COLON_MARK:
                king = king[:-1]
            #lets empty the existing allies list as someone again is asking for
            # a new allegiance, lets even empty the potential king and ruler
            cls._allies.clear()
            cls._potential_allies.clear()
            cls._potential_king = None
            cls._ruler = None
            if king:
                cls._potential_king = king

            if not cls._potential_king:
                chat_logger.info(SENDER_NOT_FOUND)
                cls.__get_input(universe=universe,kingdoms=kingdoms)

        else:
            try:
                split_message = data.split(COLON_MARK)
            except:
                chat_logger.info(PROVIDE_RIGHT_INPUT)
                cls.__get_input(universe=universe,kingdoms=kingdoms)
            else:
                try:
                    recipient_kingdom, main_message = split_message[1].split(\
                                                        COMMA)
                except:
                    chat_logger.info(PROVIDE_RIGHT_INPUT)
                    cls.__get_input(universe=universe,kingdoms=kingdoms)
                else:
                    # check if sender has been identified
                    if not cls._potential_king:
                        chat_logger.info(SENDER_NOT_FOUND)
                        cls.__get_input(universe=universe, kingdoms=kingdoms)
                    else:
                        recipient_kingdom = recipient_kingdom.strip()
                        if cls.is_msg_authentic(recipient_kingdom = \
                                                recipient_kingdom.lower(),\
                                                message = main_message,\
                                                kingdoms = kingdoms):
                            recipient_kingdom = recipient_kingdom.capitalize()
                            if recipient_kingdom not in cls._potential_allies:
                                cls._potential_allies.append(\
                                    recipient_kingdom.capitalize())
        if cls._potential_king:
            if (len(cls._potential_allies) >= len(kingdoms)/2):
                cls._ruler = cls._potential_king.capitalize()
                cls._allies = cls._potential_allies    

    
    @classmethod
    def is_msg_authentic(cls,recipient_kingdom ,message,kingdoms):
        ''' This function checks if the input message sent by the sender king
            is authentic (i.e it contains the emblem of the recipient kingdom)
            parameters:
                recipient_kingdom: The kingdom which recieves the message
                message: Message sent by the sender kingdom
                kingdoms: list of objects of all the kingdoms
        '''
        authentic = True
        #check if recipient kingdom is same as sender kingdom
        if recipient_kingdom == cls._potential_king.lower():
            chat_logger.info(SAME_SENDER_RECIEVER)
            return False
        for kingdom in kingdoms:
            if recipient_kingdom == (kingdom['name']).lower():
                emblem = kingdom['emblem'].lower()
                emblem_dict = Counter(emblem.lower())
                for key,value in emblem_dict.items():
                    match = re.findall(key,message)
                    if len(match) < value:
                        authentic = False
                        return authentic
        return authentic
    

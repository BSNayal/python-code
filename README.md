My solution is purely for the problem 1 of Set 5 'A Golden Crown'. This solution
will serve as the base for problem 2 'breaker of chains' for me.

This program works with python3+ only(doesn't work with python 2.7)
There will a lot of '\' as I followed the 80 column rule.

The program has been made in a generalized way :
- User can provide the kingdom / universe information in a json file in the
    following format:
    {
        "universe":"Southeros",
        "kingdoms": [
        {
            "name":"", 
            "king":"",
            "emblem":""
        },
        {
            "name":"",
            "king":"",
            "emblem":""
        }
        ...
    }
- Default universe is Southeros and kingdoms are fire,land,ice,air,water,land

USAGE:-
- Go to the main folder 'Set5Problem_1' and type 'python main.py'
    - This uses the default Southeros universe and its kingdoms

- User can provide an input in json format which contains the universe and the
    kingdoms which are to be used in the application

 CAUTION:- 
 - The application on start clears the console, so if you have anything on the 
    console then do save it if required, ELSE comment line no. 34 in eliza.py
    start_chat()

- 2 json files have been created for testing in the test_files folder
    - test_Southeros.json (contains Southeros and its kingdoms)
    - test_Middle_Earth.json (contains middle earth and its kingdoms, courtesy:
                                'Lord of the rings' :) )

eliza.py is the HEART of this application. it does all the parsing of the user
inputs

#TODO 
- Write test cases using unittest
- Check for memory leaks (if any)

The folder structure is as follows :-

Set5Problem_1
|
|______logs
|       |____app_logs   
|       |____chat_logs  
|
|______src
|       |____constants  
|       |____messages
|       |____utils
|
|______test
|       |____test_files
|
|______main.py
|
|______README.md        

1) logs:
    a) app_logs :- All logs related to the application (error, object creation
                    etc) will be logged in the file in this folder.
    b) chat_logs :- All the logs related to the input / output messages 
                    written or displayed on the console will be logged.

2) src
    a) constants :- It contains constants.py which has all the constants defined
    b) messages :-  It contains all the messages (error, user) to be shown or
                    logged
    c) utils :-     It contains all the utilities that are used

3) test #TODO : create automated test cases using unittest
    a) test_files :- Contains the inputs files in json format which user can 
                        provide
        

        
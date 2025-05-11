from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated, Sequence, Dict, List
from src.gameState import State
import logging

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO,filename='newfile.log')
logger = logging.getLogger()

class numberGameAgent:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(numberGameAgent, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        if numberGameAgent._instance is None:
            numberGameAgent()
        return numberGameAgent._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True

    def numberGame(self, state: State):
        number_input = state.userInput
        guess = state.guessNumber
        lowNum_ = state.lowNum
        highNum_ = state.highNum
        
        guess = (lowNum_ + highNum_) // 2
        
        if (int(number_input) == guess):
            print(f'\nNumber is {guess}')
            print('Thanks for playing.')
            print('Returning to main menu.')
            state.continueArg = 'FALSE'
            return state
        else:
            if (int(number_input) > guess):
                state.lowNum = guess
                state.guessNumber = guess
                state.continueArg = 'TRUE'
                return state
            else:
                state.highNum = guess
                state.guessNumber = guess
                state.continueArg = 'TRUE'
                return state
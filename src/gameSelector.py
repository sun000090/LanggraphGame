from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated, Sequence, Dict, List
from src.gameState import State
from src.numberGame import numberGameAgent
from src.wordGame import wordGameAgent
import logging

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO,filename='newfile.log')
logger = logging.getLogger()

class SelectorGameAgent:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SelectorGameAgent, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        if SelectorGameAgent._instance is None:
            SelectorGameAgent()
        return SelectorGameAgent._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True

    def selectorGame(self, state: State):
        print('''
Welcome to the gaming arcade. We offer the following games:
                  
    1. Number Game
    2. Word Game
    3. Exit
                  
Please select from option 1,2,3 to proceed.
            ''')
        
        userChoice = int(input())
        state.choices = userChoice
        word_games = state.wordGames
        number_games = state.numberGames
        
        if userChoice == 1:
            print('\nWelcome to the number game. Please think of a number between 1 to 50.')
            number_games += 1
            state.numberGames = number_games
            state.gamePlaying = 'number_game'
            print('\nEnter your choice: ')
            state.userInput = int(input())
            numberGameAgent().numberGame(state = state)
            return state
        elif userChoice == 2:
            print('\nWelcome to the word game. Please select a word from the given list.')
            print(["apple", "chair", "elephant", "guitar", "pizza", "tiger", "rocket", "pencil"])
            word_games += 1
            state.wordGames = word_games
            state.gamePlaying = 'word_game'
            print('\nEnter your choice: ')
            state.userChoice = input()
            wordGameAgent().wordGame(state = state)
            return state
        else:
            state.gamePlaying = 'END'
            print(f'\nThank you for playing. You played {number_games} number games and {word_games} word games')
            return state
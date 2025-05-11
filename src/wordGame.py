from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated, Sequence, Dict, List
import numpy as np
from src.gameState import State
import logging

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO,filename='newfile.log')
logger = logging.getLogger()

class wordGameAgent:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(wordGameAgent, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        if wordGameAgent._instance is None:
            wordGameAgent()
        return wordGameAgent._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True

    def wordGame(self, state: State):
        user_choice = state.userChoice
        questions = state.questions
        words = state.words

        random_numbers = np.random.choice(range(len(questions)), size=5, replace=False)
        print('\nPlease answer yes/no/maybe for these descriptive questions?')
        ques, resp = [], []
        for i in range(len(random_numbers)):
            print(questions[random_numbers[i]])
            ques.append(questions[random_numbers[i]])
            response = input('Enter your choice: ')
            resp.append(response)
        
        state.questionsAsked = ques
        state.userResponses = resp
        state.answer = np.random.choice(words)
        answers = state.answer

        print(f'\nAnswer is {answers}.')
        print('Did I guessed it right?')
        print('Enter "yes" if right or exit to main menu else "no" if you want to retry')
        responses = input('Enter your choice: ').strip().lower()

        if responses == 'yes':
            print('Returning to main menu.')
            state.continueArg = 'FALSE'
            return state
        elif responses == 'no':
            print('\nRetrying.....')
            state.wordGames += 1
            state.continueArg = 'TRUE'
            state
        else:
            print('\nReturning to main menu.')
            state.continueArg = 'FALSE'
            state
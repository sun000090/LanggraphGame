from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated, Sequence, Dict, List
import numpy as np

words = ["apple", "chair", "elephant", "guitar", "pizza", "tiger", "rocket", "pencil"]
questions = ["Is it a fruit?",
    "Is it something you can eat?",
    "Is it used for sitting?",
    "Does it have legs and a backrest?",
    "Is it a large land animal?",
    "Does it have a trunk?",
    "Is it a musical instrument?",
    "Does it have strings you can strum?",
    "Is it a type of food with toppings?",
    "Is it typically round and sliced?",
    "Is it a wild animal with stripes?",
    "Is it a carnivore that lives in jungles?",
    "Is it used for space travel?",
    "Does it launch into the sky using fuel?",
    "Is it used for writing or drawing?",
    "Does it contain graphite inside?"]

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

    def wordGame(self, user_inputs):
        def choice_record(state):
            choice_input = state['userChoice']
            questions = state['questions']
            words = state['words']

            random_numbers = np.random.choice(range(len(questions)), size=5, replace=False)
            print('\nPlease answer yes/no/maybe for these descriptive questions?')
            ques, resp = [], []
            for i in range(len(random_numbers)):
                print(questions[random_numbers[i]])
                ques.append(questions[random_numbers[i]])
                response = input('Your response: ')
                resp.append(response)
            
            state['questionsAsked'] = ques
            state['userResponse'] = resp
            state['answer'] = np.random.choice(words)
            return state
            
        def choice_checker(state):
            answer_given = state['answer']
            user_given = state['userChoice']
            if answer_given == user_given:
                print(f'\nAnswer is {user_given}. I guessed it right.')
                print('Returning to main menu.')
                return 'TRUE'
            else:
                print(f'\nAnswer is {answer_given}. I guessed it wrong.')
                print('Do you want to try again?')
                print('Or do you want to return to main menu?')
                print('Enter yes for retrying or no for returning to main menu.')
                response = input().strip().lower()
                if response == 'yes':
                    return 'FALSE'
                else:
                    return 'TRUE'
            
        class WordGameGraphState(TypedDict):
            userChoice: str
            questions : List
            words : List
            questionsAsked : List
            userResponse : List
            answer : str

        workflow = StateGraph(WordGameGraphState)

        workflow.add_node('choice_record',choice_record)

        workflow.set_entry_point("choice_record")
        workflow.add_conditional_edges("choice_record",choice_checker,{'TRUE':END,'FALSE':'choice_record'})
        
        app2 = workflow.compile()

        responses = app2.invoke({'userChoice':user_inputs,'questions':questions,'words':words},{'recursion_limit':50})
        return
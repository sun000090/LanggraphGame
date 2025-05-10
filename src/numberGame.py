from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated, Sequence, Dict, List

class numberGameAgent:
    def numberGame(user_inputs):
        def binary_search_number(state):
            number_input = state['userInput']
            lowNum = state['lowNum']
            highNum = state['highNum']

            guess = (lowNum + highNum) // 2
            state['guessNumber'] = guess

            if int(number_input) == guess:
                return state
            elif (int(number_input) > guess):
                state['lowNum'] = guess
                state['guessNumber'] = guess
                return state
            elif (int(number_input) < guess):
                state['highNum'] = guess
                state['guessNumber'] = guess
                return state
            else:
                print('Error in choice. Restart the game. Returning to main menu.')
                return state
            
        def number_checker(state):
            actual_number = state['userInput']
            guess_number = state['guessNumber']
            if int(guess_number) == int(actual_number):
                print(f'\nNumber is {guess_number}')
                print('Thanks for playing.')
                print('Returning to main menu.')
                return 'TRUE'
            else:
                return 'FALSE'
            
        class NumGameGraphState(TypedDict):
            userInput: int
            guessNumber: int
            lowNum : int
            highNum : int

        workflow = StateGraph(NumGameGraphState)

        workflow.add_node('binary_search_number',binary_search_number)

        workflow.set_entry_point("binary_search_number")
        workflow.add_conditional_edges("binary_search_number",number_checker,{'TRUE':END,'FALSE':'binary_search_number'})

        app1 = workflow.compile()

        responses = app1.invoke({'userInput':user_inputs,'lowNum':1,'highNum':50},{'recursion_limit':50})
        return
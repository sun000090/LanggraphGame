from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated, Sequence, Dict, List
from src.numberGame import numberGameAgent
from src.wordGame import wordGameAgent

class SelectorGameAgent:
    def selectorGame():
        def game_selector(state):
            print('''
            Welcome to the gaming arcade. We offer the following games:
            1. Number Game
            2. Word Game
            3. Exit
            ''')
            userChoice = int(input())
            state['choices'] = userChoice
            word_games = state['wordGames']
            number_games = state['numberGames']
            
            if userChoice == 1:
                print('\nWelcome to the number game. Please think of a number between 1 to 50.')
                number_games += 1
                state['numberGames'] = number_games
                numberGameAgent.numberGame(user_inputs=int(input()))
                return state
            elif userChoice == 2:
                print('\nWelcome to the word game. Please select a word from the given list.')
                print(["apple", "chair", "elephant", "guitar", "pizza", "tiger", "rocket", "pencil"])
                word_games += 1
                state['wordGames'] = word_games
                wordGameAgent.wordGame(user_inputs=input())
                return state
            else:
                print(f'\nYou played {number_games} number games and {word_games} word games')
                return state
            
        def interfaces(state):
            choices = state['choices']
            if (choices == 1) or (choices == 2):
                return 'TRUE'
            else:
                return 'FALSE'
            
        class SelectorGameGraphState(TypedDict):
            choices : int
            wordGames : int
            numberGames : int

        workflow = StateGraph(SelectorGameGraphState)

        workflow.add_node('game_selector',game_selector)

        workflow.set_entry_point("game_selector")
        workflow.add_conditional_edges("game_selector",interfaces,{'TRUE':'game_selector','FALSE':END})
        
        app3 = workflow.compile()

        responses = app3.invoke({'wordGames':0, 'numberGames':0},{'recursion_limit':50})
        return
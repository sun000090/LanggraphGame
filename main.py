from src.gameSelector import SelectorGameAgent
from src.numberGame import numberGameAgent
from src.wordGame import wordGameAgent
from src.gameState import State
from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated, Sequence, Dict, List
import logging

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO,filename='newfile.log')
logger = logging.getLogger()

workflows = {
    'gameSelector': SelectorGameAgent(),
    'number_game': numberGameAgent(),
    'word_game': wordGameAgent()
}

def routeGames(state: State):
    if (state.gamePlaying == 'number_game') and (state.continueArg=='TRUE'):
        return 'number_game'
    elif (state.gamePlaying == 'number_game') and (state.continueArg=='FALSE'):
        return 'gameSelector'
    elif (state.gamePlaying == 'word_game') and (state.continueArg=='TRUE'):
        return 'word_game'
    elif (state.gamePlaying == 'word_game') and (state.continueArg=='FALSE'):
        return 'gameSelector'
    elif (state.gamePlaying == 'END'):
        return END
    else:
        return 'gameSelector'
    
def buildGraph():
    works = StateGraph(State)

    works.add_node("gameSelector", workflows["gameSelector"].selectorGame)
    works.add_node("number_game", workflows["number_game"].numberGame)
    works.add_node("word_game", workflows["word_game"].wordGame)

    works.set_entry_point("gameSelector")
    works.add_conditional_edges(
            "gameSelector",
            routeGames,
            {
                "number_game": "number_game",
                "word_game": "word_game",
                "gameSelector": "gameSelector",
                END: END
            }
        )
    
    works.add_conditional_edges(
            "number_game",
            routeGames,
            {
                "number_game": "number_game",
                "word_game": "word_game",
                "gameSelector": "gameSelector",
                END: END
            }
        )
    
    works.add_conditional_edges(
            "word_game",
            routeGames,
            {
                "number_game": "number_game",
                "word_game": "word_game",
                "gameSelector": "gameSelector",
                END: END
            }
        )
    
    return works.compile()

state = State()

state.gamePlaying = ""

app1 = buildGraph()

response = app1.invoke(state,{'recursion_limit':1000})
logger.info(f'State response: {response}')
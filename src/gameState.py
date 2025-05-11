from typing import TypedDict, Annotated, Sequence, Dict, List, Optional, Any
from pydantic import BaseModel, Field

class State(BaseModel):
    currentGame: Optional[str] = ""
    wordGames: int = 0
    numberGames: int = 0
    choices: Optional[int] = 0
    userInput: Optional[int] = 0
    userChoice: Optional[str] = ""
    lowNum: int = 1
    highNum: int = 50
    guessNumber: Optional[int] = 0
    words: List = ["apple", "chair", "elephant", "guitar", "pizza", "tiger", "rocket", "pencil"]
    questions: List = ["Is it a fruit?",
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
    questionsAsked: List = []
    userResponses: List = []
    answer: Optional[str] = ""
    wordMenuResponse: Optional[str] = ""
    gamePlaying: Optional[str] = ""
    continueArg: Optional[str] = ""
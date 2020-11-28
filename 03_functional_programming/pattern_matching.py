from typing import List, Dict, Tuple
import numpy as np

# functional programming tools beyond the standard library
from pampy import match, _
from toolz.curried import *
from toolz import curry


def fibonacci(n: int) -> int:
    """Using recursion with pattern matching, to avoid conditionals"""
    return match(n,
        1, 1,
        2, 1,
        _, lambda x: fibonacci(x-1) + fibonacci(x-2)
    )

"""A pipeline for data normalization and transforming to positive, log scale which 
accumulates intermediate results. Uses partial application.
It's just a random transformation, has no real meaning.
"""

@curry
def center_data(x: List) -> np.array:
    return (
        np.array(x) - np.mean(x), 
        [{"original_data": x}]
    )

@curry 
def normalize(x: np.array, results=List[Dict]) -> Tuple[np.array, List[Dict]]:
    return (
        x / np.std(x), 
        results + [{"centered": list(x)}] 
    )

@curry
def take_log_abs(x: np.array, results: List[Dict]) -> Tuple[List, List[Dict]]:
    return (
        np.log(np.abs(x)), 
        results + [{"normalized": list(x)}]
    )

def transform(x, steps: List[str]) -> Tuple[List, List[Dict]]:
    """Can do it much nicer with a dictionary, dinamically generate the list"""
    funcs = match(steps,
        ["center", "normalize", "log"], (center_data
                                        , lambda x: normalize(x=x[0], results=x[1])
                                        , lambda x: take_log_abs(x=x[0], results=x[1])), 
        ["center", "normalize"], (center_data
                                        , lambda x: normalize(x=x[0], results=x[1])),
        _ , "undefined workflow"
    )

    return pipe(x, *funcs)

if __name__ == "__main__":
    res = transform(
        list(range(0, 15)), steps=["center", "normalize", "log"]
    )
    
    print(res)

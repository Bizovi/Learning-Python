"""An example of creating the (behavioral) strategy pattern, python specific

Strategy class: The client will use it, its method is replaced at runtime
    with a different function depending on a given `context`
"""
from typing import Callable, Optional, List, Dict, Tuple, cast, NewType
import types  # convert a normal function to have access to attributes & methods


class Strategy(object):
    """Uses a default algorithm .execute() which gets replaced at runtime
    It is closed, used by client, thus should not be modified
    """
    def __init__(self, func: Optional[Callable] = None) -> None:
        """Exploit the higher-order-function features of python"""
        if func is not None:
            # bind the function to this instance
            self.execute = types.MethodType(func, self)
            self.name = f'{self.__class__.__name__}_{func.__name__}'
        else:
            self.name = f"{self.__class__.__name__}_default"
    
    def execute(self):
        print('Default method')
        print(f'{self.name}\n')


# ==== Implement Strategies =====
def execute_replacement1(self):
    print("Replacement1 method")
    print(f'{self.name}\n')

def execute_replacement2(self):
    print("Replacement2 method")
    print(f'{self.name}\n')


def main():
    """Select the strategy at runtime: The Context"""
    s0 = Strategy()
    s0.execute()

    s1 = Strategy(execute_replacement1)
    s1.execute()

    s2 = Strategy(execute_replacement2)
    s2.execute()


if __name__ == "__main__":
    main()
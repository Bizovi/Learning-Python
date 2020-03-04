from typing import (List, Dict)


class MyObj():
    def __init__(self, repo):
        self._repo = repo
        repo.connect()
    
    def setup(self):
        self._repo.setup(cache=True, max_connections=256)
from __future__ import annotations

from collections import deque
from numpy import arange, random

class Bag:

    def __init__(self):
        self.generate()
    
    def generate(self):
        self.content = deque(random.permutation(arange(0, 7)))
    
    def pop(self):
        if not self.content:
            self.generate()
        return self.content.popleft()
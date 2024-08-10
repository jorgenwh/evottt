from typing import List
import numpy as np


class Network():
    def __init__(self, params: List):
        self.params = params

    def forward(self, x: np.ndarray) -> np.ndarray:
        for w in self.params:
            x = np.dot(x, w) 
            x = np.tanh(x)
        return x


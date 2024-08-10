import numpy as np
from ..neural.network import Network
from ..ttt.board import Board

class Genome():
    def __init__(self, network: Network):
        self.network = network

    def act(self, board: Board) -> int:
        repr = board.get_neural_representation()
        logits = self.network.forward(repr)
        return int(np.argmax(logits))

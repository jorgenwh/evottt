from dataclasses import dataclass
from .evo.population import Population


@dataclass
class Config:
    network_dims = [9, 64, 32, 16, 9]
    population_size = 500


class Manager():
    def __init__(self, config: Config):
        self.config = config

    def initialize(self):
        self.population = Population(self.config)

    def run(self):
        pass

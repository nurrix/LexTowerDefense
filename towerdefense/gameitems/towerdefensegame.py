
from abc import ABC
import tkinter as tk
import game

from enum import Enum, auto


class TowerDefenseGameState(Enum):
    IDLE = auto()
    WAITING_FOR_SPAWN = auto()
    SPAWNING = auto()



class TowerDefenseGame(game.Game):
    """ Main TowerDefense Game Class """
    
    def __init__(self):
        super().__init__(title="My Tower Defense Game", width=800, height=600, timestep=50)
        
        # Initialize TowerDefenseGame specifics
        self.initialize()
        
    def set_state(self, state: TowerDefenseGameState):
        """ Set the state of the TowerDefense"""
        self.state = state
        
    def initialize(self):
        """ Initialize the TowerDefense Game Specifics. """
        self.state: TowerDefenseGameState = TowerDefenseGameState.IDLE
        
        self.displayboard = DisplayBoard()
        self.infoboard = Infoboard()
        self.towerbox = TowerBox()
        
        self.add_object(object=Map())
        self.add_object(object=WaveGenerator())
        self.add_object(object=Mouse(self))
        
    def update(self):
        super().update()
        
    def paint(self):
        super().paint()
        
        
class DisplayBoard(ABC):
    pass

class Infoboard(ABC):
    pass

class TowerBox(ABC):
    pass

class Mouse(ABC):
    def __init__(self,master: game.Game=None):
        self.master = master

class Map(ABC):
    pass

class WaveGenerator(ABC):
    pass
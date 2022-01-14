
from abc import ABC
import tkinter as tk
from enum import Enum, auto


from engine import game, map, mouse, wavegenerator
from gameitems import towerbox, infoboard, displayboard


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
        
        self.displayboard = displayboard.DisplayBoard()
        self.infoboard = infoboard.Infoboard()
        self.towerbox = towerbox.TowerBox()
        
        self.add_object(object=map.Map())
        self.add_object(object=wavegenerator.WaveGenerator())
        self.add_object(object=mouse.Mouse(self))
        
    def update(self):
        super().update()
        
    def paint(self):
        super().paint()
        
        

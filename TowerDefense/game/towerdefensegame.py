
import tkinter as tk
import game


class TowerDefenseGame(game.Game):
    """ Main TowerDefense Game Class """
    
    def __init__(self):
        super().__init__(title="My Tower Defense Game", width=800, height=600, timestep=50)
        
        
        
    def initialize(self):
        self.displayboard = DisplayBoard()
        self.infoboard = Infoboard()
        self.towerbox = TowerBox()
        self.mouse = Mouse()
        self.gameMap = Map()
        self.wavegenerator = WaveGenerator()
        
        self.add_object(object=Map())
        self.add_object(object=WaveGenerator())
        self.add_object(object=Mouse(self))
        
    def update(self):
        super().update()
        
    def paint(self):
        super().paint()
        
        
class DisplayBoard:
    pass

class Infoboard:
    pass

class TowerBox:
    pass

class Mouse(game.GameObject):
    def __init__(self,master: game.Game=None):
        self.master = master

class Map(game.GameObject):
    pass

class WaveGenerator(game.GameObject):
    pass
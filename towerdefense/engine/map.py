import tkinter as tk

from abc import ABC
import towerdefense.engine.engine as engine

class Map(ABC):
    def __init__(self):
        pass
    
    def update(self):
        """ Update game object. """
        
    def paint(self, canvas: tk.Canvas):
        """ Paint game object. """
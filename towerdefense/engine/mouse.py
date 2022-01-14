from abc import ABC
from engine import game
import tkinter as tk

class Mouse(ABC):
    def __init__(self, master: game.Game):
        pass
    
    def update(self):
        """ Update game object. """
        
    def paint(self, canvas: tk.Canvas):
        """ Paint game object. """
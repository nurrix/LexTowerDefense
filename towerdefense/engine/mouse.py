from abc import ABC
import game as game
import tkinter as tk

class Mouse(ABC):
    def __init__(self):
        pass
    
    def update(self):
        """ Update game object. """
        
    def paint(self, canvas: tk.Canvas):
        """ Paint game object. """
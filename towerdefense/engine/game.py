

from abc import ABC, abstractmethod
import tkinter as tk
from typing import Protocol

class GameObject(Protocol):
    def update(self):
        """ Update game object. """
        
    def paint(self, canvas: tk.Canvas):
        """ Paint game object. """




class Game(ABC):
    
    def __init__(self,title:str = "Unknown Game Name", width=600, height=600, timestep:int = 50) -> None:
        """ This sets up the game"""
        self._running = False
        self.timestep = timestep
        
        
        self.root = tk.Tk()
        self.root.title(title)
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        
        self.frame = tk.Frame(master=self.root)
        self.frame.grid(row=0, column=0)
        
        self.canvas = tk.Canvas(master=self.root,
                                width=width, height=height,
                                bg="white",
                                highlightthickness=0)
        
        self.canvas.grid(
            row=0, column=0, rowspan=2, columnspan=1
        )
        
        self.objects : list[GameObject] = []
        
        
    def add_object(self, object: GameObject):
        """ add a gameobject to the objects list"""
        self.objects.append(object)    
        
    def remove_object(self, object: GameObject):
        """ remove a gameobject from the game"""
        self.objects.remove(object)
    
    def start(self) -> None:
        """ Starts main loop of gme"""
        self._running = True
        self._run()
        self.root.mainloop()
    
    def stop(self) -> None:
        self._running =False
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.root.destroy()
     
    def _run(self) -> None:
        """ run method """
        self.update()
        self.paint()
        
        if self._running:
           self.timer_id = self.root.after(ms=self.timestep, func=self._run)
    
    def update(self):
        """ This updates the game"""
        for obj in self.objects:
            obj.update()
    
    @abstractmethod
    def paint(self) -> None:
        """ This Draws the game """
        for obj in self.objects:
            obj.paint(self.canvas)
            
            
class Mouse(ABC):
    def __init__(self,master: Game=None):
        self.master = master
    
    def update(self):
        """ Update game object. """
        
    def paint(self, canvas: tk.Canvas):
        """ Paint game object. """
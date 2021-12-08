
from abc import ABC
from enum import Enum, auto

from factory.attacks import Attack

    

class AttackTypes(Enum):
    NORMAL = auto()
    SPECIAL = auto()


class Enemy(ABC):
    """
    This is an Enemy class
    """
    name: str
    health: int
    defense: int
    strength: int
    speed: int
    
    def __init__(self, name: str, health: int, defense: int, strength: int, speed: int) -> None:
        """
         
        """
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
    
    def attack(self, target):
        """
        attack generates an attack to a target.

        Args:
            target (Unit): This unit can attack a 
        """
    
    def take_damage(self, attack: Attack):
        self.health -= attack.apply_damage(self.defense)
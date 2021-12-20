
from abc import ABC, abstractmethod
from enum import Enum, auto
from utility.vector import Vector2D
from dataclasses import dataclass

from factory.attacks import Attack

    

class AttackTypes(Enum):
    NORMAL = auto()
    SPECIAL = auto()

@dataclass
class Enemy(ABC):
    """
    This is an Enemy class
    """
    Loc: Vector2D
    name: str
    health: int
    defense: int
    strength: int
    speed: int
    
    def __init__(self, Loc: Vector2D, name: str, health: int, defense: int, strength: int, speed: int, ) -> None:
        
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
        self.Loc = Loc
    
    @abstractmethod
    def attack(self, target):
        """
        attack generates an attack to a target.

        Args:
            target (Unit): This unit can attack a 
        """
    
    def take_damage(self, attack: Attack):
        self.health -= attack.apply_damage(self.defense)
        
        
class BasicEnemy(Enemy):
    """The most basic Enemy

    Args:
        Enemy ([type]): [description]
    """
    
    def __init__(self, Loc: Vector2D):
        """Initialize Basic Enemy
        """
        super().__init__(name="Basic Enemy", 
                         Loc=Loc,
                         health=100, 
                         defense=0, 
                         strength=0, 
                         speed=10,
                         )
        
    def attack(self, target):
        pass
        
        
class EnemyFactory(ABC):
    """ A abstract class factory to generate Enemies """
    @abstractmethod
    def create_new_unit(self, Loc: Vector2D) -> Enemy:
        """ Return a Unit """
        

class BasicEnemyFactory(EnemyFactory):
    """ Factory aimed to generate Basic Enemy"""
    
    def create_new_unit(self, Loc: Vector2D) -> BasicEnemy:
        """ Create an Enemy instance"""
        return BasicEnemy(Loc = Loc)
    
    

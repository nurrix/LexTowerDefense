from abc import ABC, abstractmethod
from dataclasses import dataclass
from sys import intern
from this import d

from factory.attacks import Attack, ProjectileAttack, AttackType
from factory.enemies import Enemy
from utility.vector import Vector2D

@dataclass
class Unit(ABC):
    Loc: Vector2D
    strength: int
    health: int
    defense: int
    range: int
    splash_radius: int
    can_attack_flying: bool
    attack_type: AttackType
    dmg_lvl: int = 0
    
    @abstractmethod
    def attack(self, target: Enemy) -> Attack:
        """ Make an attack """
    
    @abstractmethod
    def take_damage(self, attack: Attack) -> None:
        """ Unit takes damage """

class Tower(Unit):
    """
    Tower creates an instance of a tower
    """
    def __init__(self, Loc: Vector2D, strength:int, health:int, defense: int, range:int, splash_radius:int, can_attack_flying:bool) -> None:
        super().__init__(Loc=Loc,
                         strength=strength, 
                         health=health, 
                         defense=defense,
                         range=range, 
                         splash_radius=splash_radius, 
                         can_attack_flying=can_attack_flying, 
                         attack_type = AttackType.Projectile,
                         )
        
    def attack(self, target: None) -> ProjectileAttack:
        return ProjectileAttack(attack_strength=self.strength, 
                                Loc=self.Loc, 
                                velocity=10.0,
                                target=target, 
                                ignore_defense=False, 
                                splash_radius=self.splash_radius,
                                piercing = False,
                                dmg_lvl=self.dmg_lvl)
    
    def take_damage(self, attack: Attack) -> None:
        self.health -= attack.apply_damage(self.defense)
    
class SimpletonTower(Tower):
    """ Class for the Simpleton Tower """
    def __init__(self, Loc: Vector2D,) -> None:
        super().__init__(Loc=Loc,
                         strength=1, 
                         health=1, 
                         defense=0,
                         range=10, 
                         splash_radius=0, 
                         can_attack_flying=True)

class UnitFactory(ABC):
    """ A factory to generate Units """
    
    @abstractmethod
    def create_new(self) -> Unit:
        """ Return a Unit """
        
class TowerFactory(UnitFactory):
    """ Factory aimed to generate a SimpletonTower"""
    @abstractmethod
    def create_new(self) -> Tower:
        """ Creates a new tower intance """
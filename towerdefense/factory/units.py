from abc import ABC, abstractmethod
from dataclasses import dataclass

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
    price: int
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
    def __init__(self, Loc: Vector2D, 
                 strength:int, 
                 health:int, 
                 defense: int, 
                 range:int, 
                 splash_radius:int, 
                 can_attack_flying:bool, 
                 price: int) -> None:
        """ Initializes a tower"""
        super().__init__(Loc=Loc,
                         strength=strength, 
                         health=health, 
                         defense=defense,
                         range=range, 
                         splash_radius=splash_radius, 
                         can_attack_flying=can_attack_flying,
                         price = price, 
                         attack_type = AttackType.Projectile,
                         )
        
    def attack(self, target: None) -> ProjectileAttack:
        """ Attack a target"""
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
                         range=20, 
                         splash_radius=0, 
                         can_attack_flying=True,
                         price=10,)
        
class SplashTower(Tower):
    """ Class for Splash Tower """
    def __init__(self, Loc: Vector2D) -> None:
        super().__init__(Loc=Loc, 
                         strength=1, 
                         health=1, 
                         defense=0, 
                         range=10, 
                         splash_radius=1, 
                         can_attack_flying=False, 
                         price=20,)
class UnitFactory(ABC):
    """ A factory to generate Units """
    
    @abstractmethod
    def create_new_unit(self, Loc: Vector2D) -> Unit:
        """ Return a Unit """
        
class TowerFactory(UnitFactory):
    """ Factory aimed to generate a Tower"""
    @abstractmethod
    def create_new_unit(self, Loc: Vector2D) -> Tower:
        """ Creates a new tower intance """
        
class SimpletonTowerFactory(TowerFactory):
    """ Factory aimed to generate Simpleton Tower Instances"""
    
    def create_new_unit(self, Loc: Vector2D) -> Tower:
        """ Create a Simpleton Tower instance"""
        return SimpletonTower(Loc = Loc)

class SplashTowerFactory(TowerFactory):
    """ Factory aimed to generate Splash Tower Instances"""
    
    def create_new_unit(self, Loc: Vector2D) -> Tower:
        """ Create a Splash Tower instance"""
        return SplashTower(Loc = Loc)

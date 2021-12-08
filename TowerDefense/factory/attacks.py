
from dataclasses import dataclass
from enum import Enum, auto

from utility.vector import Vector2D

class AttackType(Enum):
    Projectile = auto()
    Melee = auto()

@dataclass
class Attack:
    attack_strength: int
    Loc: Vector2D
    velocity: float
    target: None
    ignore_defense: bool = False
    splash_radius: int = 0
    piercing: bool = False
    dmg_lvl: int = 0
    _dmg_amplifier = 0.1
    
    def apply_damage(self, target_defense: int) -> int:
        dmg_dealt = self.calculate_damage(target_defense = target_defense)
        return dmg_dealt
    
    def calculate_damage(self, target_defense: int) -> int:
        dmg_dealt = self.dmg_lvl * self._dmg_amplifier * self.attack_strength - target_defense * self.ignore_defense
        dmg_dealt = int(dmg_dealt) if dmg_dealt>=0 else 0
        return dmg_dealt
        
@dataclass   
class MeleeAttack(Attack):
    pass
    
        
@dataclass
class ProjectileAttack(Attack):
    pass

from dataclasses import dataclass
from typing import Optional

from TowerDefense.utility.vector import Vector2D

@dataclass
class Projectile:
    attack_strength: int
    ignore_defense: bool
    Loc: Vector2D
    velocity: Vector2D
    destination: Vector2D
    
    def apply_damage(self, target_defense: int = False) -> int:
        dmg_dealt = self.attack_strength - target_defense * self.ignore_defense
        dmg_dealt = dmg_dealt if dmg_dealt>=0 else 0
        return dmg_dealt
        
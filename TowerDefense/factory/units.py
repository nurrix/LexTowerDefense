from abc import ABC, abstractmethod

from TowerDefense.factory.attack import Projectile


class Unit(ABC):
    strength: int
    health: int
    range: int
    @abstractmethod
    def attack(self, target) -> Projectile:
        """ Make an attack """
    
    def take_damage(self, attack: Projectile) -> None:
        """ Unit takes damage """


class UnitFactory(ABC):
    """ A factory to generate Units """
    
    @abstractmethod
    def create_new(self) -> Unit:
        """ Return a Unit """
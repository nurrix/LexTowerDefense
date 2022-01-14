#!/usr/bin/env python


from factory.enemies import BasicEnemyFactory
from factory.units import SimpletonTowerFactory, SplashTowerFactory
from utility.vector import Vector2D

from gameitems import towerdefensegame


def main() -> None:
    """
        This function starts our program.
    """
    # Test by creating a Tower
    unit_factory = {
            "SimpleTower": SimpletonTowerFactory(),
            "SplashTower": SplashTowerFactory(),
        }
    
    enemy_factory = {"BasicEnemy": BasicEnemyFactory(),}
    
    game = towerdefensegame.TowerDefenseGame()
    game.start()
    game.stop()
    
    
    simpletower = unit_factory["SimpleTower"].create_new_unit(Loc=Vector2D(x=100, y=313))
    splashtower = unit_factory["SplashTower"].create_new_unit(Loc=Vector2D(x=100, y=313))
    basicenemy = enemy_factory["BasicEnemy"].create_new_unit(Loc=Vector2D(x=100,y=300))
    
    print(simpletower)
    print(splashtower)
    print(basicenemy)
    

if __name__ == "__main__":
    main()

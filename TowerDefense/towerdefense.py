#!/usr/bin/env python


from factory.units import SimpletonTower, SimpletonTowerFactory, SplashTowerFactory
from utility.vector import Vector2D


def main() -> None:
    """
        This function starts our program.
    """
    # Test by creating a Tower
    factory = {"SimpleTower": SimpletonTowerFactory(),
               "SplashTower": SplashTowerFactory(),
            }
    
    simpletower = factory["SimpleTower"].create_new_unit(Loc=Vector2D(x=100, y=313))
    splashtower = factory["SplashTower"].create_new_unit(Loc=Vector2D(x=100, y=313))
    print(simpletower)
    print(splashtower)
    

if __name__ == "__main__":
    main()

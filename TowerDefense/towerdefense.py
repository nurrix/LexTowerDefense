#!/usr/bin/env python


from factory.units import SimpletonTower
from utility.vector import Vector2D


def main() -> None:
    """
        This function starts our program.
    """
    # Test by creating a Tower
    tower1 = SimpletonTower(Vector2D(x=100,y=100))
    print(tower1)
    

if __name__ == "__main__":
    main()

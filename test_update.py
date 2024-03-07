import pytest
from game import Game  # replace with your actual module name
import pygame
def test_update():
    # create an instance of MyClass
    my_obj = Game()

    # move the object such that it will collide with a wall
    my_obj.x = 10
    my_obj.y = 10

    # create a mock wall list
    walls = [pygame.Rect(0, 0, 10, 10), pygame.Rect(0, 0, 10, 10)]

    # set the walls attribute of the object to the mock wall list
    my_obj.walls = walls

    # call the update method
    my_obj.update()

    # assert that the object has moved back
    assert my_obj.x == 9
    assert my_obj.y == 10

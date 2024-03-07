import pygame
from player import Player

def test_move_right():
    # create an instance of MyClass
    my_obj = Player(10,10)

    # set the initial position of the object
    my_obj.position = [10, 10]

    # set the speed of the object
    my_obj.speed = 1

    # call the move_right method
    my_obj.move_right()

    # assert that the object has moved to the right by its speed
    assert my_obj.position == [11, 10]
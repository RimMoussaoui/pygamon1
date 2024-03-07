import pygame
from player import Player

def test_move_left():
    # create an instance of Player
    my_obj = Player(10,10)

    # set the initial position of the object
    my_obj.position = [10, 10]

    # set the speed of the object
    my_obj.speed = 1

    # call the move_left method
    my_obj.move_left()

    # assert that the object has moved to the left by its speed
    assert my_obj.position == [9, 10]
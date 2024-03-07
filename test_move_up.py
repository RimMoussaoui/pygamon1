import pygame
from player import Player

def test_move_up():
    # create an instance of Player
    my_obj = Player(10,10)

    # set the initial position of the object
    my_obj.position = [10, 10]

    # set the speed of the object
    my_obj.speed = 1

    # call the move_up method
    my_obj.move_up()

    # assert that the object has moved up by its speed
    assert my_obj.position == [10, 9]
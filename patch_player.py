import pygame
from unittest.mock import patch
from player import Player

def test_player():
    mock_surface = pygame.Surface([32, 32])
    with patch('pygame.image.load') as mock_load:
        mock_load.return_value = mock_surface
        player = Player(0, 0)
        assert player.sprite_sheet == mock_surface
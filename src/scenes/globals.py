import pygame

from src.scenes.messaging import Messaging
from src.scenes.resources.ship_resources import ShipResources

"""
This file essentially just makes globals.resources a singleton
"""
pygame.init()
resources = ShipResources()
messaging = Messaging()

""" Container for the game class, which manages the lifetime of the game """
import pygame
from pygame.locals import QUIT

from .settings import Settings
from .window import WIN
from .util import Color

class Game:
    """ Packages together every element of the game for ease of use """
    def __init__(self, settings_file):
        self.settings = Settings(settings_file)

        self.window = WIN(self.settings.window)
        self.clock = pygame.time.Clock()
        self.game_settings = self.settings.game

        self.running = False

    def _init(self) -> None:
        """ Handles all the initialization that needs to happen before the game starts """
        self.running = True

    def _loop(self) -> None:
        """ This is everything that happens every frame """
        self.clock.tick(self.game_settings["FPS"])
        delta_time: int = self.clock.get_time() / 10

        self.window.fill(Color.black)

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

        self.window.draw.rect(Color.yellow, (
            self.window.width / 2, self.window.height / 2, 100, 300
        ))

        self.window.update()

    def _destroy(self) -> None:
        """ Handles everything that needs to be done before the game closes """

    def run(self) -> None:
        """
            This is the only public method of the class, and it just calls all the
        lifetime methods in the correct order and manner.
        """
        self._init()
        while self.running:
            self._loop()
        self._destroy()

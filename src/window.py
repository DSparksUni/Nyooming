""" Container for the WIN class, serving as a wrapper for the pygame window """
import pygame
from pygame.locals import RESIZABLE

from src.util import Color

class WIN:
    """ Container class that handles basic window operations """

    class Draw:
        """ Simple class to mimic the pygame API to draw primitives """
        def __init__(self, screen: pygame.Surface):
            self.screen = screen

        def rect(
            self, color: Color,
            rectangle: pygame.Rect | tuple[int, int, int, int],
            width: int = 0
        ) -> None:
            """
                Function that passes the arguments through to pygame's
            built-in rectangle drawing function

            Args:
                color(Color): Color to draw the rectangle with
                rectangle(pygame.Rect | tuple[int, int, int, int]):
                    Position of the topleft corner of the rectangle,
                    along with the width and height
                *width(int): Thickness with which to draw the rectangle
                    (fills the rectangle if 0)
            """
            pygame.draw.rect(self.screen, color, rectangle, width)

        def line(
            self, color: Color,
            pos1: tuple[int, int], pos2: tuple[int, int],
            width: int = 1
        ) -> None:
            """
                Function that passes the arguments through to pygame's
            built-in line drawing function

            Args:
                color(Color): Color to draw the line with
                pos1(tuple[int, int]): Position to begin drawing the line
                pos2(tuple[int, int]): Position to stop drawing the line
                *width(int): Thickness with which we draw the line
            """
            pygame.draw.line(self.screen, color, pos1, pos2, width)

    def __init__(self, settings) -> None:
        #Initialize the window, as well as the storage for width and height
        self.width = settings["width"]
        self.height = settings["height"]
        self.window = pygame.display.set_mode((self.width, self.height), RESIZABLE)
        pygame.display.set_caption(settings["title"])

        #Initialize the screen, which is where everything will be drawn
        self.screen = pygame.Surface((self.width, self.height))

        # Initialize draw object (Although it may seem to have no reason for
        #existing, it allows for a similar use as pygame's API)
        self.draw = self.Draw(self.screen)

    def blit(self, surf: pygame.Surface, pos: tuple[int, int]) -> None:
        """
            Makes the blit method on a normal pygame window surface available for
        this container class.

        Args:
            surf(pygame.Surface): Surface to draw on the window
            pos(tuple[int, int]): Place to put the top left corner of the surface
        """
        self.screen.blit(surf, pos)

    def fill(self, color: Color) -> None:
        """
            Makes the fill method on a normal pygame window surface available for
        this container class.

        Args:
            color(Color): Color to fill the window with
        """
        self.screen.fill(color)

    def update(self) -> None:
        """ Draws the screen to the window, and then updates the window """
        self.window.blit(self.screen, (0, 0))
        pygame.display.update()

    def resize(self, new_width: int, new_height: int) -> None:
        """
            Resizes the screen and window

            Args:
                new_width(int): The width to resize the window to
                new_height(int): The height to resize the window to
        """
        self.screen = pygame.transform.scale(self.screen, (new_width, new_height))
        self.window = pygame.display.set_mode((new_width, new_height), RESIZABLE)

        self.width = new_width
        self.height = new_height

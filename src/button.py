""" Container for the Button class, as well as the ButtonDrawingStrategy class """

from dataclasses import dataclass

import pygame

from .util import Color

@dataclass(frozen=True)
class ButtonDrawingStrategy:
    """ Draw strategy for a button """
    font: pygame.font
    border_color: Color = Color.white
    body_color: Color = Color.yellow
    text_color: Color = Color.white
    text_size: int = 0

class Button:
    """ Class that creates rectangular text buttons for use in the game """
    def __init__(
        self, rect: tuple[int, int, int, int] | pygame.Rect,
        text: str, draw_strategy: ButtonDrawingStrategy
    ):
        self.rect = rect
        self.text = text
        self.draw_strategy = draw_strategy

    def draw(self, window: pygame.Surface) -> None:
        """
            Renders the button onto the provided surface

        Args:
            WIN(pygame.Surface): Surface to draw the button on
        """
        #Draw the border
        pygame.draw.rect(window, self.draw_strategy.border_color, self.rect)

        #Draw the body
        pygame.draw.rect(
            window, self.draw_strategy.body_color,
            (self.rect.x + 5, self.rect.y + 5, self.rect.width - 10, self.rect.height - 10)
        )

        #Draw the text


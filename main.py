""" Simple startoff place that just instantiates the game class and runs it """
from src.game import Game

if __name__ == '__main__':
    Game("settings.json").run()
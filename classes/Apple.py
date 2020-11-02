import random
from classes.Game import Game


class Apple(Game):
    def __init__(self, INITIAL_POSITION):
        self.__coords = INITIAL_POSITION

    def change_position(self):
        self.__coords = (
            random.randint(1, self.WINDOW_WIDTH / self.UNIT_SIZE) *
            self.UNIT_SIZE,
            random.randint(1, self.WINDOW_HEIGHT / self.UNIT_SIZE) *
            self.UNIT_SIZE)

    def get_coords(self):
        return self.__coords
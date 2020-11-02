class Game:
    OI = '0I'
    UNIT_SIZE = 10
    DIRECTIONS = {'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 800
    GAME_BOUNDARIES = ((0, WINDOW_WIDTH), (0, WINDOW_HEIGHT))
    COLORS = {
        'BLACK': (0, 0, 0),
        'WHITE': (255, 255, 255),
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0)
    }

    FPS = 12
    PIXEL_SIZE = (UNIT_SIZE, UNIT_SIZE)

    def __init__(self):
        self.__GAME_STATUS = 1

        self.__SCORE = 0

    def set_game_status(self, status):
        if type(status) != int:
            print('O status do game de ver um número (0, 1 ou 2)')
        else:
            self.__GAME_STATUS = status

    def get_game_status(self):
        return self.__GAME_STATUS

    def get_score(self):
        return self.__SCORE

    def increase_score(self):
        self.__SCORE += 1

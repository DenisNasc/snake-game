from classes.Game import Game


class Snake(Game):
    def __init__(self, INITIAL_POS, SNAKE_HEAD_IMAGE):
        self.__coords = INITIAL_POS
        self.__SNAKE_HEAD_IMAGE = SNAKE_HEAD_IMAGE
        self.__snake_direction = 1

    def set_coords(self, new_coord):
        self.__coords = self.__coords.append(new_coord)

    def get_coords(self):
        return self.__coords

    def get_snake_head_image(self):
        return self.__SNAKE_HEAD_IMAGE

    def is_snake_in_boundaries(self):
        snakeHeadCoords = self.__coords[0]

        i = 0

        for (min, max) in self.GAME_BOUNDARIES:
            if snakeHeadCoords[i] > max or snakeHeadCoords[i] < min:
                return False
            i += 1

        return True

    def set_direction(self, NEW_DIRECTION):
        if self.__snake_direction == 0 and self.DIRECTIONS[NEW_DIRECTION] == 2:
            return
        if self.__snake_direction == 1 and self.DIRECTIONS[NEW_DIRECTION] == 3:
            return
        if self.__snake_direction == 2 and self.DIRECTIONS[NEW_DIRECTION] == 0:
            return
        if self.__snake_direction == 3 and self.DIRECTIONS[NEW_DIRECTION] == 1:
            return

        self.__snake_direction = self.DIRECTIONS[NEW_DIRECTION]

    def move_snake(self):
        snake_head_coord = self.__coords[0]
        snake_direction = self.__snake_direction
        unit_size = self.UNIT_SIZE

        newDirections = [
            (snake_head_coord[0], snake_head_coord[1] - unit_size),
            (snake_head_coord[0] + unit_size, snake_head_coord[1]),
            (snake_head_coord[0], snake_head_coord[1] + unit_size),
            (snake_head_coord[0] - unit_size, snake_head_coord[1])
        ]

        for (_, value) in self.DIRECTIONS.items():
            if snake_direction == value:
                self.__coords[0] = newDirections[value]

        for i in range(len(self.__coords) - 1, 0, -1):
            self.__coords[i] = (self.__coords[i - 1][0],
                                self.__coords[i - 1][1])

    def add_body(self):
        self.__coords.append((self.__coords[-1][0] - self.UNIT_SIZE,
                              self.__coords[-1][1] - self.UNIT_SIZE))

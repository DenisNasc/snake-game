import pygame, sys
from pygame.locals import *

sys.path.append('/home/denis/Documentos/developer/python/snake-game/classes')

from classes.Game import Game
from classes.Snake import Snake
from classes.Apple import Apple

pygame.init()

# GAME INITIALIZATION
snake_game = Game()

WINDOW_SIZE = (snake_game.WINDOW_WIDTH, snake_game.WINDOW_HEIGHT)
PIXEL_SIZE = snake_game.PIXEL_SIZE
COLORS = snake_game.COLORS
FPS = snake_game.FPS

# AUDIO
pygame.mixer.init()
pygame.mixer.music.load('./assets/audios/yamete-kudasai.wav')

# SNAKE INITIALIZATION
snake_head_image = pygame.image.load('./assets/images/snake-head.png')
initial_snake_pos = [(200, 200), (190, 200), (180, 200)]

snake = Snake(initial_snake_pos, snake_head_image)

# APPLE INITIALIZATION
initial_apple_pos = (100, 100)

apple = Apple(initial_apple_pos)

# CREATING A WINDOW FOR THE GAME
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

# SURFACES

snake_body_surface = pygame.Surface(PIXEL_SIZE)
snake_body_surface.fill(COLORS['GREEN'])

apple_surface = pygame.Surface(PIXEL_SIZE)
apple_surface.fill(COLORS['RED'])

clock = pygame.time.Clock()

# is_snake_in_boundaries

while pygame.get_init():
    clock.tick(FPS)
    game_status = snake_game.get_game_status()

    pygame.display.set_caption(str(snake_game.get_score()))

    for event in pygame.event.get():
        if event.type == QUIT:

            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake.set_direction('UP')
            if event.key == K_RIGHT:
                snake.set_direction('RIGHT')
            if event.key == K_DOWN:
                snake.set_direction('DOWN')
            if event.key == K_LEFT:
                snake.set_direction('LEFT')

    if game_status == 1:
        snake.move_snake()
        is_snake_in_boundaries = snake.is_snake_in_boundaries()

        if is_snake_in_boundaries == False:
            snake_game.set_game_status(0)
            print('PERDEU!')

        if snake.get_coords()[0] == apple.get_coords():
            print('GANHOU')
            pygame.mixer.music.play()
            snake_game.increase_score()
            apple.change_position()
            snake.add_body()

        WINDOW.fill(COLORS['BLACK'])

        WINDOW.blit(apple_surface, apple.get_coords())

        for coord in snake.get_coords():
            WINDOW.blit(snake_body_surface, coord)

    if game_status == 0:
        pygame.display.set_caption('Você perdeu :(')

    pygame.display.update()

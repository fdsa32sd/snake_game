import msvcrt
import os

# direction of the snake
# 0 = stop
# 1 = up
# 2 = down
# 3 = right
# 4 = left
direction = 0

# position of the snake and its tail
snake = [[3, 3]]

food = [0, 0]
food_exists = False

score = 0


def get_user_input():
    return msvcrt.getch()


# draw snake on map and return the drawn result
def plot_snake(map):
    return map


# draw walls on map and return the drawn result
def generate_wall(map):
    return map


def generate_food(map):
    return map


def check_colision():
    colision = False
    return colision


def check_food_colision():
    colision = False
    return colision


def move_snake():
    pass


def clear_screen():
    # on mac or linux use clear instead cls
    os.system("cls")


# main game loop
while not check_colision():
    pass

import msvcrt
import os
import multiprocessing
import random

def get_user_input():
    return msvcrt.getch()


# draw snake on map and return the drawn result
def plot_snake(map, snake):
    for snake_body in snake:
        map[snake_body[0]][snake_body[1]] = "O"

# draw walls on map and return the drawn result
def generate_wall():
    map = []
    map.append(list("#"*65))
    for y in range(25):
        space = list(" "*63)
        row = ["#"]
        row = row + space
        row.append("#")
        map.append(row)
    map.append(list("#"*65))
    return map


def generate_food(map, food):
    map[food[0]][food[1]] = "X"

def check_colision(snake):
    head = snake[0]
    hit_tail = head in snake[1:] 
    hit_wall = head[0] < 1 or head[0] > 24 or head[1] < 1 or head[1] > 64
    return hit_tail or hit_wall


def check_food_colision(snake, food):
    head = snake[0]
    return food == head


def move_snake(snake, direction, ate_food):
    head = snake[0]
    next = []
    if direction == 1:
        next = [head[0]-1, head[1]]
    elif direction == 2:
        next = [head[0]+1, head[1]]
    elif direction == 3:
        next = [head[0], head[1]+1]
    elif direction == 4:
        next = [head[0], head[1]-1]
    if len(next) != 0:
        snake.insert(0, next)
        if not ate_food:
            snake.pop()

def clear_screen():
    # on mac or linux use clear instead cls
    os.system("cls")

def print_map(map):
    result = ""
    for row in map:
        for character in row:
            result = result + character
        result = result + "\n"
    print(result)

def game_controls(input_data_store):
    input_val = get_user_input()
    if input_val == b"w":
        input_data_store.put(1)
    elif input_val == b"s":
        input_data_store.put(2)
    elif input_val == b"d":
        input_data_store.put(3)
    elif input_val == b"a":
        input_data_store.put(4)

def process_controls(direction):
        input_data_store = multiprocessing.Queue()
        input_process = multiprocessing.Process(target=game_controls, args=[input_data_store])
        input_process.start()
        input_process.join(0.1)
        input_process.terminate()
        if input_data_store.empty():
            return direction
        else:
            return input_data_store.get()

# main game loop
def game_loop():
    # direction of the snake
    # 0 = stop (used only for when starting the game)
    # 1 = up
    # 2 = down
    # 3 = right
    # 4 = left
    direction = 0

    # position of the snake and its tail
    snake = [[3, 3], [3, 2]]

    food = [0, 0]
    food_exists = False

    score = 0
    while not check_colision(snake):
        map = generate_wall()
        if food_exists:
            if check_food_colision(snake, food):
                score += 10
                food = [random.randint(1, 24), random.randint(1, 64)]
                move_snake(snake, direction, True)
            else:
                move_snake(snake, direction, False)
        else:
            food = [random.randint(1, 24), random.randint(1, 64)]
            food_exists = True
        generate_food(map, food)
        plot_snake(map, snake)
        print_map(map)
        print("Score:", score)
        direction = process_controls(direction)
        clear_screen()

if __name__ == '__main__':
    game_loop()

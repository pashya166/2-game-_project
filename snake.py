from tkinter import *
import random

GAME_WIDHTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class SnakeGame:
    pass

class food:
    pass

def next_turn():
    pass

def chanege_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

Label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
Label.pack()

Canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDHTH)
Canvas.pack()

window.update()

window_widht = window.winfo_width()
window.mainloop()
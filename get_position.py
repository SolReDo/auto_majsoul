import numpy as np

def get_position_xy(hand_titles,choice):
    for title in hand_titles:
        if title[0] == choice:
            x,y = title[1]
            return x,y
        
import pyautogui
import cv2
from tempdict import get_templates
from get_hand_area import get_hand_area
from recognize_hand import recognize_hand
game_screen = pyautogui.locateOnScreen('game_screen.png',confidence=0.5)
x,y,w,h = game_screen
print(f"game_screen area: x = {x},y = {y},w = {w},h = {h},")

templates = get_templates()

hand_area = get_hand_area(game_screen)
x,y,w,h = hand_area

print(f"hand_area: x = {x},y = {y},w = {w},h = {h},")

hand_area = tuple(map(int, hand_area))
game_screen = tuple(map(int, game_screen))
hand_titles = recognize_hand(hand_area,templates)
print('手牌为：',[title[0] for title in hand_titles])
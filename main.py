import pyautogui
from tempdict import get_templates
from get_hand_area import get_hand_area
from recognize_hand import recognize_hand
from crawler import get_most_powerful
from format_hands import format_hands
from get_position import get_position_xy
from hu_or_zimo import judge_rong
import time

#截取游戏界面，获取游戏界面区域坐标
game_screen = pyautogui.locateOnScreen('game_screen.png',confidence=0.5)
x,y,w,h = game_screen
print(f"game_screen area: x = {x},y = {y},w = {w},h = {h},")

#初始化模板
templates = get_templates()

#获取手牌区域坐标
hand_area = get_hand_area(game_screen)
x,y,w,h = hand_area
print(f"hand_area: x = {x},y = {y},w = {w},h = {h},")

#参数格式转换
hand_area = tuple(map(int, hand_area))
game_screen = tuple(map(int, game_screen))

while True:
    judge_rong('hu.png',0.7)
    judge_rong('zi_mo.png',0.7)

    #读取手牌
    hand_titles = recognize_hand(hand_area,templates)
    hands = [title[0] for title in hand_titles]
    n = len(hands)
    if n == 14:
        #手牌格式转换
        hands = format_hands(hands)
        print('手牌为：',hands)

        #获取最高牌效率打法
        choice = get_most_powerful(hands)
        print(f'打出{choice}的牌效率最高')

        #获取对应坐标
        x_pos,y_pos = get_position_xy(hand_titles,choice)
        print(f'出牌坐标为x:{x_pos},y:{y_pos}')
    
        #鼠标操作——出牌
        pyautogui.moveTo(x_pos,y_pos,0.2)
        pyautogui.click(clicks=2,interval=0.2)
        pyautogui.move(0,100)

        time.sleep(0.2)
import pyautogui
import cv2
from get_hand_area import get_hand_area
from recognize_hand import recognize_hand
game_screen = pyautogui.locateOnScreen('game_screen.png',confidence=0.5)
x,y,w,h = game_screen
print(f"game_screen area: x = {x},y = {y},w = {w},h = {h},")


templates = {
    
    '1m':cv2.imread('mahjong_list/1m.png',cv2.IMREAD_COLOR),
    '2m':cv2.imread('mahjong_list/2m.png',cv2.IMREAD_COLOR),
    '3m':cv2.imread('mahjong_list/3m.png',cv2.IMREAD_COLOR),
    '4m':cv2.imread('mahjong_list/4m.png',cv2.IMREAD_COLOR),
    '5m':cv2.imread('mahjong_list/5m.png',cv2.IMREAD_COLOR),
    '6m':cv2.imread('mahjong_list/6m.png',cv2.IMREAD_COLOR),
    '7m':cv2.imread('mahjong_list/7m.png',cv2.IMREAD_COLOR),
    '8m':cv2.imread('mahjong_list/8m.png',cv2.IMREAD_COLOR),
    '9m':cv2.imread('mahjong_list/9m.png',cv2.IMREAD_COLOR),

    
    '1p':cv2.imread('mahjong_list/1p.png',cv2.IMREAD_COLOR),
    '2p':cv2.imread('mahjong_list/2p.png',cv2.IMREAD_COLOR),
    '3p':cv2.imread('mahjong_list/3p.png',cv2.IMREAD_COLOR),
    '4p':cv2.imread('mahjong_list/4p.png',cv2.IMREAD_COLOR),
    '5p':cv2.imread('mahjong_list/5p.png',cv2.IMREAD_COLOR),
    '6p':cv2.imread('mahjong_list/6p.png',cv2.IMREAD_COLOR),
    '7p':cv2.imread('mahjong_list/7p.png',cv2.IMREAD_COLOR),
    '8p':cv2.imread('mahjong_list/8p.png',cv2.IMREAD_COLOR),
    '9p':cv2.imread('mahjong_list/9p.png',cv2.IMREAD_COLOR),

    
    '1s':cv2.imread('mahjong_list/1s.png',cv2.IMREAD_COLOR),
    '2s':cv2.imread('mahjong_list/2s.png',cv2.IMREAD_COLOR),
    '3s':cv2.imread('mahjong_list/3s.png',cv2.IMREAD_COLOR),
    '4s':cv2.imread('mahjong_list/4s.png',cv2.IMREAD_COLOR),
    '5s':cv2.imread('mahjong_list/5s.png',cv2.IMREAD_COLOR),
    '6s':cv2.imread('mahjong_list/6s.png',cv2.IMREAD_COLOR),
    '7s':cv2.imread('mahjong_list/7s.png',cv2.IMREAD_COLOR),
    '8s':cv2.imread('mahjong_list/8s.png',cv2.IMREAD_COLOR),
    '9s':cv2.imread('mahjong_list/9s.png',cv2.IMREAD_COLOR),

    '1z':cv2.imread('mahjong_list/1z.png',cv2.IMREAD_COLOR),
    '2z':cv2.imread('mahjong_list/2z.png',cv2.IMREAD_COLOR),
    '3z':cv2.imread('mahjong_list/3z.png',cv2.IMREAD_COLOR),
    '4z':cv2.imread('mahjong_list/4z.png',cv2.IMREAD_COLOR),
    '5z':cv2.imread('mahjong_list/5z.png',cv2.IMREAD_COLOR),
    '6z':cv2.imread('mahjong_list/6z.png',cv2.IMREAD_COLOR),
    '7z':cv2.imread('mahjong_list/7z.png',cv2.IMREAD_COLOR),

}

hand_area = get_hand_area(game_screen)
x,y,w,h = hand_area

print(f"hand_area: x = {x},y = {y},w = {w},h = {h},")

hand_area = tuple(map(int, hand_area))
game_screen = tuple(map(int, game_screen))
hand_titles = recognize_hand(hand_area,templates)
print('手牌为：',[title[0] for title in hand_titles])
import pyautogui

def judge_rong(image_path,confidence):
    try:
        he = pyautogui.locateOnScreen(image_path,confidence=confidence)
        x,y,w,h = he
        he_x = x+int(0.5*w)
        he_y = y+int(0.5*h)
        print(f'可以和牌 按钮坐标为x:{he_x} y:{he_y}')
        pyautogui.moveTo(he_x,he_y,0.2)
        pyautogui.click()
    except:
        print('此时没有到达胡牌要求')
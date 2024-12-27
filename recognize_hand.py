import pyautogui

def recognize_hand(hand_region, templates):
    hand_tiles = []
    seen_positions = set()
    threshold = 87
    for title_name, title in templates.items():
        # 使用 pyautogui 定位模板图像
        try:
            results = pyautogui.locateAllOnScreen(title, region=hand_region, confidence=0.8)
            for result in results:
                center_x = result.left + result.width // 2
                center_y = result.top + result.height // 2
                # 用一个阈值来判断两个位置是否相近
                position = (center_x, center_y)
                
                # 如果该位置之前没有出现过，就将其添加到结果中
                if not any(abs(position[0] - p[0]) < threshold and abs(position[1] - p[1]) < threshold for p in seen_positions):
                    seen_positions.add(position)  # 记录这个位置
                    hand_tiles.append((title_name, result))  # 保存麻将牌及其位置
        except:
            continue
    
    return hand_tiles
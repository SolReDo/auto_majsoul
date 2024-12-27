def get_hand_area(game_window):
    # 获取手牌位置
    x, y, w, h = game_window
    hand_region = (x, y + int(0.8 * h), w, int(0.25 * h))  # 调整手牌位置
    return hand_region
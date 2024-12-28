from collections import defaultdict

def format_hands(hands):
    groups = defaultdict(list)

    # 按字母后缀分组
    for item in hands:
        number, suffix = item[:-1], item[-1]  # 提取数字和字母
        groups[suffix].append(number)

    # 构建最终字符串
    result = ''.join(''.join(numbers) + suffix for suffix, numbers in groups.items())

    return result


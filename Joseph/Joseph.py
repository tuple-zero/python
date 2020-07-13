import Joseph.Josephus as jo


def out_circle(in_list, in_num, start_index=1):
    """
    :param in_list:人物信息输入
    :param in_num:游戏规则
    :param start_index:开始位置
    :return: 返回淘汰的顺序
    """
    joseph = jo.Josephus()
    in_len = len(in_list)
    count = 0
    move = start_index - 1

    while in_len > 0:
        count += 1
        if move == in_len:
            move = 0
        if count == in_num:
            joseph.add_joseph(in_list.pop(move))
            count = 0
            move -= 1
            in_len -= 1
        move += 1
    return joseph
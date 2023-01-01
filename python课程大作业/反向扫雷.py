"""
目标:
    给出含有"地雷"的网格图(用'x'表示雷,'.'表示空单元格)
    输出另一幅网格图:
        其中每个位置都是一个数字,表示其周围八个单元格内'雷'的数量。
        地雷(x)不再出现。
        不与任何地雷接壤的位置和地雷都显示为空单元格'.'。
输入:
    第一行:一个整数,表示网格的宽度
    第二行:一个整数,表示网格的高度
    接下来的行:字符串,表示网格图
示例:
    输入:                       输出:
    16                          
    9                           
    ................            ................
    ................            ................
    ................            ................
    ................            ................
    ................            ...111..........
    ....x...........            ...1.1..........
    ................            ...111..........
    ................            ................
    ................            ................
"""

w = int(input("请输入地图宽度:"))
h = int(input("请输入地图高度:"))


def get_mines() -> list:
    mines = []
    for i in range(h):
        line = input()
        for j in range(w):
            if line[j] == 'x':
                mines.append([i, j])
    return mines


def get_answer(w: int, h: int, mines: list):
    # 创建一个二维列表来储存答案
    answer = []
    for i in range(h):
        answer.append([0]*w)

    for mine in mines:
        # 一个雷周围的雷数量不可能超过8,结果中的负数一定是雷
        answer[(mine[0])][(mine[1])] = -10
        for i in {-1, 1, 0}:
            for j in {-1, 1, 0}:
                if (0 <= mine[0]+i < h) and (0 <= mine[1]+j < w):
                    answer[mine[0]+i][mine[1]+j] += 1

    for i in range(h):
        for j in range(w):
            if answer[i][j] <= 0:
                # 不与任何地雷接壤的位置和地雷都显示为空单元格'.'
                answer[i][j] = '.'

    return answer


def print_answer(ans):
    for line in ans:
        print(*line, sep='')


if __name__ == '__main__':
    mines = get_mines()
    answer = get_answer(w, h, mines)
    print_answer(answer)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
ME,OPP,NONE = [1,0,-1]
my_matter = 0
opp_matter = 0

# map[y][x]来获取单元格信息
# map[行][列]
map = [[] for j in range(height)]

class cell:

    x:int
    y:int
    scrap_amount: int
    owner: int
    units: int
    recycler: bool
    can_build: bool
    can_spawn: bool
    in_range_of_recycler: bool

    def __init__(self, x,y,informations: list[int]) -> None:
        self.x = x
        self.y = y
        self.scrap_amount = informations[0]
        self.owner = informations[1]
        self.units = informations[2]
        self.recycler = bool(informations[3])
        self.can_build = bool(informations[4])
        self.can_spawn = bool(informations[5])
        self.in_range_of_recycler = bool(informations[6])
    def buid_here(self) -> str:
        return f'BUILD {self.x} {self.y}'
    def spawn_here(self,amount) -> str:
        return f'SPAWN {amount} {self.x} {self.y}'
    def move_to(self,amount,x,y) -> str:
        return f'MOVE {amount} {self.x} {self.y} {x} {y}'


def game_loop():
    while True:
        # 更新数据
        # matter 材料数 十个材料可以建造一个回收站或一个robot
        my_matter, opp_matter = [int(i) for i in input().split()]
        update_map()
        # my_cells, opp_cells ,my_units, opp_units, my_recyclers, opp_recyclers , grass
        my_cells, opp_cells, my_units, opp_units, my_recyclers, opp_recyclers, grass = sort_out()  # 分拣

        commonds = build(my_cells) + spawn(my_cells) + move(my_units, opp_units)
        print(';'.join(commonds) if len(commonds) > 0 else 'WAIT')


def update_map() -> None :
    for i in range(height):
        for j in range(width):
            # scrap_amount: 可获得的零件数
            # owner: 1 = me, 0 = foe, -1 = neutral
            # unit: 该单位上有多少机器人
            map[i].append(cell(j,i,[int(k) for k in input().split()]))

def sort_out() -> list[list[cell]]:
    my_cells = [] 
    opp_cells = []  
    my_units = [] 
    opp_units = [] 
    my_recyclers = []
    opp_recyclers = [] 
    grass = []
    for line in map:
        for cell in line:
            if cell.owner == ME:
                my_cells.append(cell)
                if cell.units > 0:
                    my_units.append(cell)
                elif cell.recycler:
                    my_recyclers.append(cell)
            elif cell.owner == OPP:
                opp_cells.append(cell)
                if cell.units > 0:
                    opp_units.append(cell)
                elif cell.recycler:
                    opp_recyclers.append(cell)
            else:
                grass.append(cell)
    return [my_cells, opp_cells, my_units, opp_units, my_recyclers, opp_recyclers, grass]

# 用来判断是否要建造以及在哪里建造===========================

def build(my_cells:list[cell]) -> list[str]:
    build_commonds = []
    for cell in my_cells:
        if cell.can_build:
            # TODO:判断是不是要在这里BUILD
            my_matter -= 10 # type: ignore
            build_commonds.append(cell.buid_here()) 
    return build_commonds
    

# spawn 规划生产机器人======================================

def spawn(my_cells: list[cell]) -> list[str]:
    spawn_commonds = []
    for cell in my_cells:
        if my_matter // 10 == 0:
            return spawn_commonds
        if cell.can_spawn:
            # TODO:是否要在这里spawn 及数量
            cell.spawn_here(1)
    return spawn_commonds

# 规划每个机器人的移动=====================================


def move(my_units: list[cell], opp_units:list[cell]) -> list[str]:
    move_commonds = []
    for unit in my_units:
        move_commonds.append(unit.move_to(unit.units,opp_units[0].x,opp_units[0].y))
    return move_commonds

if __name__ == '__main__':
    game_loop()

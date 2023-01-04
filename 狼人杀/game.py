'''
思路:
    先实现简单的游戏循环
流程:
    1. 天黑请闭眼
    2. 特殊角色行动时间
    3. 天亮
    4. 发言
    5. 投票
'''
import random
from identity import *



class game(object):
    players:list[player]
    def __init__(self,players:list[player]) -> None:
        pass        # TODO: 初始化 ,连接玩家

    def game_init(self):
        for each in preinstall_1:
            l = random.sample(self.players,each.number)
            for i in l:
                i.job = each.name
                self.send_msg([i],f'your job is {i.job}')
        # pass #TODO 确定各个玩家身份

    def gameloop(self): # TODO 主循环
        self.send_msg(self.players,'天黑请闭眼')



    def send_msg(self,recever:list[player],contect:str):
        '''
        发消息
        两个参数:
            recever : 接收者列表
            contect : 内容
        方法: 将内容发送给recever中的每一个,类似print()方法
        '''
        pass

    def get_resp(self,recever:player,contect:str):
        '''
        响应
        两个参数:同上
        方法:将内容发送给recever中的每一个,并等待直至对方回复,返回回复内容
        '''
        pass    # TODO 获取响应
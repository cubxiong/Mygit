# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:39:56 2018

@author: Cub
"""

#Game2048--2048小游戏

import random
import time
import pyHook

class Game2048():
    def __init__(self,xnum=4,ynum=4):
        '''生成初始化二维列表'''
        self.xnum=xnum
        self.ynum=ynum
        self.score=0
        self.randdata=[2,4] #初始化随机数，只能为2或4
        self.data=[[0 for i in range(0,xnum)] for i in range(0,ynum)] #生成初始化二维列表
        
    def trans(self,lista): 
        '''转置二维列表'''
        return([[row[i] for row in lista] for i in range(len(lista[0]))])

    def createdata(self):
        '''从二维列表中值为Q0的位置随机选择一个填上2或4'''
        zeros=[]  #创建空列表用于存放为0的位置信息
        for i in range(0,self.xnum):
            for j in range(0,self.ynum):
                if (self.data[i][j]==0):
                    zeros.append((i,j))
        self.thisposition=random.choice(zeros) #从0的列表中随机选择一个位置tuple
        self.data[self.thisposition[0]][self.thisposition[1]]=random.choice(self.randdata)
    
    def left(self):
        '''左滑处理，将所有非0数字按从左往右顺序排列'''
        firstzero=0 #记录每行第一个0的位置
        for i in range(0,len(self.data)):  #按行处理
            for j in range(0,len(self.data[0])):
                if (self.data[i][j]==0):
            
    
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
        self.score=0   #初始化得分为0
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
    
    def left(self,transdata):
        '''左滑处理，将所有非0数字按从左往右顺序排列'''
        self.transdata=transdata
        for i in range(0,len(self.transdata)):  #按行处理
            firstzero=None #记录每行第一个0的位置,初始为空
            for j in range(0,len(self.transdata[0])):
                if (self.transdata[i][j]==0): #如果是0值的处理
                    if(j==0):  
                        firstzero=j  #如果最左为0值，则firstzero=0
                    elif(self.transdata[i][j-1]>0): #左侧是非0值
                        firstzero=j
                elif(firstzero !=None):  #如果是非零值且firstzero不为空
                    self.transdata[i][firstzero]=self.transdata[i][j]
                    self.transdata[i][j]=0
                    firstzero+=1
        return(self.transdata)
    
    def right(self,transdata):
        '''右滑处理，将所有非0数字按从右往左顺序排列'''
        self.transdata=transdata
        for i in range(0,len(self.transdata)):  #按行处理
            firstzero=None #记录每行第一个0的位置
            for j in range(-1,-len(self.transdata[0])-1,-1):  #按从右到左的顺序处理
                if (self.transdata[i][j]==0): 
                    if(j==-1):
                        firstzero=j
                    elif(self.transdata[i][j+1]>0):
                        firstzero=j
                elif(firstzero !=None):
                    self.transdata[i][firstzero]=self.transdata[i][j]
                    self.transdata[i][j]=0
                    firstzero-=1
        return(self.transdata)

    def up(self):
        '''上滑处理，等于将转置后矩阵按左滑处理,处理完后再转置回去'''
        transdata=self.trans(self.data)
        self.left(transdata)
        return(self.trans(transdata))
        
    def down(self):
        '''下滑处理，等于将转置后矩阵按右滑处理,处理完后再转置回去'''
        transdata=self.trans(self.data)
        self.right(transdata)
        return(self.trans(transdata))
        
    def lmerge(self,transdata):
        '''向左合并处理'''
        self.transdata=transdata
        for i in range(0,len(self.transdata)):  #按行处理
            for j in range(1,len(self.transdata[0])):  #从第二位开始
                if(self.transdata[i][j]>0):  #当前值大于0就进行处理
                    if(self.transdata[i][j-1]==self.transdata[i][j]):  #当前值与左邻值相等
                        self.transdata[i][j-1]=self.transdata[i][j]*2
                        self.score=self.score+self.transdata[i][j]
                        self.transdata[i][j]=0
                        
    def rmerge(self,transdata):
        '''向右合并处理'''
        self.transdata=transdata
        for i in range(0,len(self.data)):  #按行处理
            for j in range(-2,-len(self.data[0])-1,-1):  #从右边第二位开始
                if(self.data[i][j]>0):  #当前值大于0就进行处理
                    if(self.data[i][j+1]==self.data[i][j]):  #当前值与右邻值相等
                        self.data[i][j+1]=self.data[i][j]*2
                        self.score=self.score+self.data[i][j]
                        self.data[i][j]=0
                        
                        
    def umerge(self):
        '''上滑合并，等于将转置后矩阵按左合并处理,处理完后再转置回去'''
        transdata=self.trans(self.data)
        self.lmerge(transdata)
        return(self.trans(transdata))
        
    def dmerge(self):
        '''下滑合并，等于将转置后矩阵按右合并处理,处理完后再转置回去'''
        transdata=self.trans(self.data)
        self.rmerge(transdata)
        return(self.trans(transdata))
        
    def show(self):
        #输出前的处理
        #判断输赢，并输出得分
        #先将棋盘数据转为1维列表data1便于统计
        data1=sum(self.data,[])
        #统计看棋盘上是否有2048的数字，如有则赢
        if(data1.count(2048)>=1):
            print("恭喜，您赢了！3秒后程序关闭！")
            print("您的得分是："+str(self.score))
            time.sleep(3)
            exit(0)
        if(data1.count(0)==0):
            print("棋盘已满，您输啦！3秒后程序关闭！")
            print("您的得分是："+str(self.score))
            time.sleep(3)
            exit(0)
        #如果尚未输赢，则继续输出棋盘
        #输出对应的棋盘
        print("您的当前累计得分是："+str(self.score))
        print("------------------------------------------")
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[0])):
                print(str(self.data[i][j]),end="\t")
            print()
        print("------------------------------------------")

    def listenanddo(self,mypresskey):
        #获取当前按键
        thiskey=mypresskey.Key
        if (thiskey=="F10"):
            #启动或重启程序
            self.data=[[0 for i in range(0,self.xnum)] for i in range(0,self.ynum)]
            self.createdata()
            self.show()
        elif(thiskey=="Escape"):
            print("您是否需要终止程序？如需要，可以按Ctrl+C实现")
        elif(thiskey=="Left"):
            #左移具体过程左滑处理、左滑合并、合并后左滑处理、随机生成数据、棋盘展示
            self.left(self.data)
            self.lmerge(self.data)
            self.left(self.data)
            self.createdata()
            self.show()
        elif(thiskey=="Right"):
            #右移具体过程右滑处理、右滑合并、合并后右滑处理、随机生成数据、棋盘展示
            self.right(self.data)
            self.rmerge(self.data)
            self.right(self.data)
            self.createdata()
            self.show()
        elif(thiskey=="Up"):
            #左移具体过程上滑处理、上滑合并、合并后上滑处理、随机生成数据、棋盘展示
            self.up()
            self.umerge()
            self.up()
            self.createdata()
            self.show()
        elif(thiskey=="Down"):
            #右移具体过程下滑处理、下滑合并、合并后下滑处理、随机生成数据、棋盘展示
            self.down()
            self.dmerge()
            self.down()
            self.createdata()
            self.show()
        return True

    def main(self):
        '''主控程序'''
        hook=pyHook.HookManager()
        #监听所有按键
        hook.KeyDown=self.listenanddo
        hook.HookKeyboard()
        
    
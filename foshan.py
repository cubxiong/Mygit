# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:57:42 2018
佛山语音数据预处理

@author: Cub
"""

#import linecache
#for i in range(200):
#    the_line=linecache.getline(r"g:\Temp\moc46200-46300",i)
#    print(i,' ')
#    print(type(the_line),len(the_line))

def getdata(fn,sellist,getlist,linelen=2952):
    '''获取fn中linelen长度的行中的selist指定的列，追加到getlist列表中'''
    with open(fn,'rt',encoding='utf-8') as filename:
        for line in filename.readlines()[0:200]:
            if (len(line)==linelen):
                if(line[2:9]!='cs_aiu_'):
                    tmplist=[]
                    curline=line.replace(" ","").strip().split("|")
                    for i in sellist:
                        tmplist.append(curline[i])
#                    tmplist.append(curline[20])
#                    tmplist.append(curline[23])
#                    tmplist.append(curline[24])
#                    tmplist.append(curline[18])
#                    tmplist.extend(curline[46:49])
#                    tmplist.append(curline[114])
                    getlist.append(tmplist)
    return(getlist)

moc_fn=r'g:\Temp\moc46200-46300'
moc_list=[20,23,24,18,46,47,48,114]
moc_data=[['moc.msisdn','moc.lac','moc.ci','moc.calledno','moc.pd','moc.fail','moc.cause','moc_dt']] #初始moc表头

print(getdata(moc_fn,moc_list,moc_data,linelen=2952))

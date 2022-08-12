# -*- coding: utf-8 -*-
# @Time    : 2022/8/3 18:25
# @Author  : JingBW
# @Site    : 
# @File    : main.py
# @Software: PyCharm 
# @Comment :

import sys
# 把项目路径加入python搜索路径 可以在cmd运行
sys.path.append('D:\Software\PyCharm\pythonProject\\test01')

from summer_2022.wordDictation.tool import getWrong_Input_outOrder, getWrong_Input_countBack, sendMail, reMes, \
    getReviseList, reWrong_Input, getNewBookL


def run():
    # 0关闭，1开启

    revise = eval(input('是否开启复习模式，0：关闭，1：开启\n'))#复习模式
    if revise ==0:#如果不开启复习模式，则判断是否需要选择必修二的课本 如果为0则自动进入必修一的课本
        theSencondBook = eval(input('是否是必修二及以上课本：0：不是，1：是的\n'))
    else:#如果开启复习模式 那么就不要再看是否需要theSencondBook必修二了
        theSencondBook = 0
    #倒序 无序开一个就可以
    countBack = 0 #倒数
    out_of_order = 0 #无序
    #确保无序和倒序只选择一种
    if countBack ==1:
        out_of_order =0
    elif out_of_order ==1:
        countBack =0
    if revise ==1:
        print('准备进去复习模式...')
    filePath = input("请输入文件路径：")
    fileName = filePath.split('\\')[-1]  # 根据路径获取当前文件名字
    if revise ==0 and theSencondBook ==0:
        # 返回的列表里面包含 0：错误的 1：输入的
        if out_of_order == 1 :
            list = getWrong_Input_outOrder(1,filePath)#调用无序则直接输入1
        elif countBack == 1 :
            list = getWrong_Input_countBack(filePath)#倒序
        else:
            list = getWrong_Input_outOrder(0,filePath)#正序
    elif revise ==1:
        print('==========已进入复习模式=====================')
        # 返回的list包含 0：英语和1：汉语的列表
        # 参数1：是否无序 参数2：文件路径
        reviseList = getReviseList(1,filePath)
        list = reWrong_Input(reviseList)
    elif theSencondBook ==1:
        print('==========已进入必修二及以上课本=====================')
        list = getNewBookL(out_of_order,filePath)
        list = reWrong_Input(list)

    #给错题&输入的列表 返回做好格式的信息
    p = reMes(fileName,list)
    #根据信息发邮件
    sendMail(fileName,p)

if __name__ == '__main__':
    run()
    input("输入回车键结束")


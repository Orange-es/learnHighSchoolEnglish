# -*- coding: utf-8 -*-
# @Time    : 2022/8/3 18:25
# @Author  : JingBW
# @Site    : 
# @File    : main.py
# @Software: PyCharm 
# @Comment :
from summer_2022.wordDictation.tool import getWrong_Input_outOrder, getWrong_Input_countBack, sendMail, reMes

if __name__ == '__main__':
    # 0关闭，1开启
    #倒序 无序开一个就可以
    countBack = 0 #倒数
    out_of_order = 0 #无序
    #确保只选择一种
    if countBack ==1:
        out_of_order =0
    elif out_of_order ==1:
        countBack =0
    filePath = input("请输入文件路径：")
    fileName = filePath.split('\\')[-1]  # 根据路径获取当前文件名字
    # 返回的列表里面包含 0：错误的 1：输入的
    if out_of_order == 1 :
        list = getWrong_Input_outOrder(1,filePath)#调用无序则直接输入1
    elif countBack == 1 :
        list = getWrong_Input_countBack(filePath)#倒序
    else:
        list = getWrong_Input_outOrder(0,filePath)#正序

    #给错题&输入的列表 返回做好格式的信息
    p = reMes(fileName,list)
    #根据信息发邮件
    sendMail(fileName,p)
    input("输入回车键结束")


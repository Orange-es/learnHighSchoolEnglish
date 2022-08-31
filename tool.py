# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 10:41
# @Author  : JingBW
# @Site    : 
# @File    : tool.py
# @Software: PyCharm 
# @Comment :
import os
import random
import smtplib
from email.mime.text import MIMEText


#遍历文件夹所有文件
def findEveryFile(filePath):
    i=0
    l = []
    for filepath, dirnames, filenames in os.walk(filePath):
        for filename in filenames:
            # print(filename)
            # print(filepath)
            i=i+1
            print(i,':',os.path.join(filepath, filename))
            l.append(os.path.join(filepath, filename))
    return l

#用于必修二及以上的解析
def getNewBookL(out_of_order, filePath):
    data = []  # 读取出来的存入data
    list = []  # 分解的英语和汉语存入list
    file = open(filePath, 'r', encoding='UTF-8')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        data.append(row)

    # data是每行的列表
    # 进行随机抽取的话
    # python避免随机元素重复可以使用random模块的sample()函数，
    # 它返回一个新列表，新列表存放随机不重复的元素。
    if out_of_order == 1:
        print('\n已开启无序模式.....')
        data = random.sample(data, len(data))
    # ===========================================

    enList = []
    chList = []
    for i in range(len(data)):
        # num = data[i].split('.',1)[0]#编号
        # print('编号：',num)
        try:
            noNum = data[i].split('.', 1)[1].lstrip()  # 去掉编号并取除头部空格
            # print('去掉编号:',noNum)
            # print('去掉编号并取除头部空格:',noNum.lstrip())
            en = noNum.split('  ', 1)[0]  # 英文
            # print('en:',en)
            ch = noNum.split('  ', 1)[1].strip()  # 汉语
            # print('ch:',ch)
            enList.append(en)
            chList.append(ch)
        except:
            print('文件出错：',data[i],'\n')
            pass

    #print('英语：', enList)
    #print('汉语：', chList)
    if len(enList) == len(chList):
        list.append(enList)
        list.append(chList)
    else:
        print('长度不相等！')
    return list


#获取到英语汉语的列表后
#返回错题&输入的列表
def reWrong_Input(list):
    wrongList = []  # 错误集合
    inputList = []  # 输入集合 可能会输入会与原答案差标点符号 亦作对比
    enList = list[0]
    chList = list[1]
    if len(enList) == len(chList):
        print('本次测试共有：', len(enList), '个单词，每个单词最多错误三次\n下面开始测试：')
        for i in range(len(enList)):
            print('\n====================================')
            print('第', i + 1, '/', len(enList), '个')
            # print(enList[i])
            # print(chList[i])
            print('汉语：', chList[i])
            print('请输入正确的拼写：')
            t = 1  # 判断单词输入是否错误 继续进行输入
            num = 0  # 判断错误次数
            while t:
                if num == 3:
                    print('已错误三次，正确拼写为：\n', enList[i])
                    wrongWord = '英语：' + enList[i] + '-汉语：' + chList[i]
                    wrongList.append(wrongWord)
                    break
                inputEn = input()
                if remove(enList[i]) == remove(inputEn):
                    t = 0
                    print('输入正确，请继续....\n')
                else:
                    t = 1
                    num = num + 1
                    if num < 3:
                        print("已错", num, "次，请继续输入正确的拼写：")
                    if num == 3:
                        print("已错", num, "次，请看正确答案。")
                        # 把输入的和正确的存入inputList
                        # 可能会输入会与原答案差标点符号亦作对比
                        word = '英语：' + enList[i] + '-汉语：' + chList[i]
                        word = '输入的：' + inputEn + '</br>正确的：' + word
                        inputList.append(word)  # 这是第三次已经输入 所有直接加入列表

    print('\n一共错了', len(wrongList), '个。\n可能会有误差，最终请看邮箱。\n')
    print('错误列表：', wrongList)
    print('输入的错误列表及正确：', inputList)
    list.append(wrongList)
    list.append(inputList)
    return list

def getReviseList(out_of_order,filePath):
    data = [] #读取出来的存入data
    list=[] #分解的英语和汉语存入list
    file = open(filePath, 'r', encoding='UTF-8')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        data.append(row)
    #==================没看懂,但可以用==========================================
    data = [x.strip() for x in data if x.strip() != '']
    # print('newData:',data)
    # for x in data:
    #     if x.strip() != '':
    #         x = x.strip()
    #         b = [x]
    #         print(b)
    #==============================================================

    #data是每行的列表
    #进行随机抽取的话
    # python避免随机元素重复可以使用random模块的sample()函数，
    # 它返回一个新列表，新列表存放随机不重复的元素。
    if out_of_order ==1:
        print('\n已开启无序模式.....')
        data=random.sample(data,len(data))
    #===========================================


    enList = []
    chList = []
    for i in range(len(data)):
        en = data[i].split('-')[0]
        ch = data[i].split('-')[1]
        enList.append(en)
        chList.append(ch)
    #print('英语：',enList)
    #print('汉语：',chList)
    if len(enList) == len(chList):
        list.append(enList)
        list.append(chList)
    else:
        print('长度不相等！')

    return list


#获取错题&输入 列表 返回需要发送邮件的信息
def reMes(fileName,list):
    wrongList = list[0]
    inputList = list[1]
    p = '<h5>' + fileName + '错题本</h5>'
    if len(inputList) ==0:
        #等于0 证明没有错的
        print('没有错的')
        inputList.append('没有错误的 厉害了')
        wrongList.append('没有错误的 厉害了')
    for i in range(len(wrongList)):#错误集合
        p = p + '<p>' + wrongList[i] + '</p>'
    p = p + '<h5>输入的集合''可能与原答案相差标点符号亦作对比</h5>'
    for i in range(len(inputList)):#输入的集合
        p = p + '<p>' + inputList[i] + '</p>'
    return p


def getList(out_of_order,filePath):
    data = [] #读取出来的存入data
    list=[] #分解的英语和汉语存入list
    file = open(filePath, 'r', encoding='gbk')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        # tmp_list = row.strip().split('\n') #按‘，’切分每行的数据
        # tmp_list[-1] = tmp_list[-1].replace('\n','').replace('\t','').replace(r"'\t","").strip() #去掉换行符
        # data.append(tmp_list) #将每行数据插入data中

        #mes = row.strip()
        # print(type(mes))
        data.append(row)
    #print(len(data))
    # print(data[0])#1.	exchange 	/?ks?t?e?nd?/ 	n.  交换; 交流  vt.  交换; 交流；交易; 兑换
    # print(data[0].split('/')[0])#1.	exchange

    #data是每行的列表
    #进行随机抽取的话
    # python避免随机元素重复可以使用random模块的sample()函数，
    # 它返回一个新列表，新列表存放随机不重复的元素。
    if out_of_order ==1:
        print('\n已开启无序模式.....')
        data=random.sample(data,len(data))
    #===========================================


    enList = []
    chList = []
    for i in range(len(data)):
        en = data[i].split('/')[0].split('.', 1)[1].strip()
        if len(data[i].split('/')) == 1:  # =1 则证明是词组，没有/ 没办法进行分割
            # senior high school 			（美国）高中
            # 按照空格分    0：英语  1：汉语
            tempEn = ''
            for j in range(len(en.split(" ")) - 1):
                tempEn = tempEn + ' ' + en.split(" ")[j]
            tempCh = en.split(" ")[-1].strip()
            #print('英语:', tempEn)
            #print('汉语:', tempCh)
            enList.append(tempEn)
            chList.append(tempCh)
            #print(i, '----------------------------------------')
            continue  # 跳过当前继续执行下一个循环
            # break  直接中断循环，不再执行
            # pass 什么都不操作，接着循环
        try:
            ch = data[i].split('/')[2].strip()
            #print('英语：', en)
            #print('汉语：', ch)  # n.  交换; 交流  vt.  交换; 交流；交易; 兑换
            enList.append(en)
            chList.append(ch)
            #print(i, '----------------------------------------')
        except Exception as e:
            print('错误：\n',data[i])
            pass
    list.append(enList)
    list.append(chList)
    return list




def sendMail(title,text):
    #设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.qq.com'
    # 163用户名
    mail_user = '3523531883@qq.com'
    # 密码(部分邮箱为授权码)
    mail_pass = 'ddqcufwgjbqpchjc'
    # 邮件发送方邮箱地址
    sender = '3523531883@qq.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['786788651@qq.com']

    # 设置email信息
    # 邮件内容设置
    #message = MIMEText(texe, 'plain', 'utf-8')
    message = MIMEText(text,'html','UTF-8')
    # 邮件主题
    message['Subject'] = '英语单词_'+title
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('Mailsuccess')
    except smtplib.SMTPException as e:
        print('Mailerror', e)  # 打印错误


#删除所有空格
def remove(string):
    return "".join(string.split());

#无序模式
def getWrong_Input_outOrder(out_of_order,filePath):#无序模式
    list = getList(out_of_order, filePath)
    list = reWrong_Input(list)
    return list

#倒序模式
def getWrong_Input_countBack(filePath):
    #选择倒序 则无序直接为0 即不选择无序
    wrongList = []  # 错误集合
    inputList = []  # 输入集合 可能会输入会与原答案差标点符号 亦作对比
    list = getList(0, filePath)
    enList = list[0]
    chList = list[1]
    if len(enList) == len(chList):
        print('\n已开启倒序模式...')
        print('本次测试共有：', len(enList), '个单词，每个单词最多错误三次\n下面开始测试：')
        for i in range(len(enList)-1,-1,-1):
            print('\n====================================')
            print('第', i + 1, '/', len(enList), '个')
            # print(enList[i])
            # print(chList[i])
            print('汉语：', chList[i])
            print('请输入正确的拼写：')
            t = 1  # 判断单词输入是否错误 继续进行输入
            num = 0  # 判断错误次数
            while t:
                if num == 3:
                    print('已错误三次，正确拼写为：\n', enList[i])
                    wrongWord = '英语：' + enList[i] + '-汉语：' + chList[i]
                    wrongList.append(wrongWord)
                    break
                inputEn = input()
                if remove(enList[i]) == remove(inputEn):
                    t = 0
                    print('输入正确，请继续....\n')
                else:
                    t = 1
                    num = num + 1
                    if num < 3:
                        print("已错", num, "次，请继续输入正确的拼写：")
                    if num == 3:
                        print("已错", num, "次，请看正确答案。")
                        # 把输入的和正确的存入inputList
                        # 可能会输入会与原答案差标点符号亦作对比
                        word = '英语：' + enList[i] + '-汉语：' + chList[i]
                        word = '输入的：' + inputEn + '</br>正确的：' + word
                        inputList.append(word)  # 这是第三次已经输入 所有直接加入列表

    print('\n一共错了', len(wrongList), '个。\n可能会有误差，最终请看邮箱。\n')
    print('错误列表：', wrongList)
    print('输入的错误列表及正确：', inputList)

    list.append(wrongList)
    list.append(inputList)
    return list
# -*- coding: utf-8 -*-
# @Time    : 2022/8/3 20:49
# @Author  : JingBW
# @Site    : 
# @File    : tool.py
# @Software: PyCharm 
# @Comment :
import smtplib
from email.mime.text import MIMEText
from email.header import Header




#根据文件读取单词 并进行分割
def getList(filePath):
    data = []
    list=[]
    file = open(filePath, 'r', encoding='gbk')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    i = 0
    for row in file_data:
        # tmp_list = row.strip().split('\n') #按‘，’切分每行的数据
        # tmp_list[-1] = tmp_list[-1].replace('\n','').replace('\t','').replace(r"'\t","").strip() #去掉换行符
        # data.append(tmp_list) #将每行数据插入data中

        mes = row.strip()
        # print(type(mes))
        data.append(row)
    #print(len(data))
    # print(data[0])#1.	exchange 	/?ks?t?e?nd?/ 	n.  交换; 交流  vt.  交换; 交流；交易; 兑换
    # print(data[0].split('/')[0])#1.	exchange
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
        ch = data[i].split('/')[2].strip()
        #print('英语：', en)
        #print('汉语：', ch)  # n.  交换; 交流  vt.  交换; 交流；交易; 兑换
        enList.append(en)
        chList.append(ch)
        #print(i, '----------------------------------------')
    list.append(enList)
    list.append(chList)
    return list




def sendMail(text):
    #设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.qq.com'
    # 163用户名
    mail_user = '3523531883'
    # 密码(部分邮箱为授权码)
    mail_pass = 'ddqcufwgjbqpchjc'
    # 邮件发送方邮箱地址
    sender = '3523531883@qq.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['3523531883@qq.com']

    # 设置email信息
    # 邮件内容设置
    #message = MIMEText(texe, 'plain', 'utf-8')
    message = MIMEText(text,'html','UTF-8')
    # 邮件主题
    message['Subject'] = '英语_错误单词'
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
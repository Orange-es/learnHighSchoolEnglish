# -*- coding: utf-8 -*-
# @Time    : 2022/8/3 18:25
# @Author  : JingBW
# @Site    : 
# @File    : main.py
# @Software: PyCharm 
# @Comment :
import smtplib
from email.mime.text import MIMEText






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
    receivers = ['3523531883@qq.com','3077288566@qq.com']

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

if __name__ == '__main__':
    wrongList = []  # 错误集合
    inputList = [] #输入集合 可能会输入会与原答案差标点符号 亦作对比
    filePath = input("请输入文件路径：")
    fileName = filePath.split('\\')[-1]  # 根据路径获取当前文件名字
    list = getList(filePath)
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
                    if num <3:
                        print("已错", num, "次，请继续输入正确的拼写：")
                    if num ==3:
                        print("已错", num, "次，请看正确答案。")
                        #把输入的和正确的存入inputList
                        #可能会输入会与原答案差标点符号亦作对比
                        word = '英语：' + enList[i] + '-汉语：' + chList[i]
                        word = '输入的：' +inputEn+'</br>正确的：'+word
                        inputList.append(word)  #这是第三次已经输入 所有直接加入列表

    print('\n一共错了',len(wrongList),'个。\n可能会有误差，最终请看邮箱。\n')
    print('错误列表：', wrongList)
    print('输入的错误列表及正确：',inputList)
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
    sendMail(fileName,p)
    input("输入回车键结束")


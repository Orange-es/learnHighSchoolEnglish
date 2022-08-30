# -*- coding: utf-8 -*-            
# @Time : 2022/8/30 22:18
# @Author :JingBW
# @FileName: testCET4Format.py
# @Software: PyCharm

#字符串中删除数字
def dNum(s):
    newstring = ''.join([i for i in s if not i.isdigit()])
    print(newstring.replace(' ','',1))
    return newstring.replace(' ','',1)

#一行一行读取方法 给一个路径 返回一个集合
def read(filePath):
    f=open(filePath,encoding='utf-8')
    line = f.readline().strip() #读取第一行
    txt=[]
    txt.append(line)
    while line:  # 直到读取完文件
       line = f.readline().strip()  # 读取一行文件，包括换行符
       txt.append(line)
    f.close()  # 关闭文件
    return txt
# txt = read('unit1.txt')
# print(txt)
# t = []
# for i in range (len(txt)):
#     s = dNum(txt[i])
#     t.append(s)

#一行一行写入方法 给一个文件路径，一个集合
def write(filePath,t):
    # -*-coding:utf8-*-# encoding:utf-8
    for i in  range (len(t)):
        f = open(filePath, 'a',encoding='utf-8')
        f.write(str(t[i]) + '\n')
        f.close()


if __name__ == '__main__':
    #先读取文件
    txt = read('test.txt')
    print(txt)
    #去掉数字
    t = []
    for i in range (len(txt)):
        s = dNum(txt[i])
        t.append(s)
    #删除文件 以便下次创建再写入
    # if os.path.exists('test.txt'): os.remove('test.txt')




    # l = read('test.txt')
    list = []
    for i in range(len(t)):
        s = t[i].replace('adv.', '-adv.', 1)
        s = s.replace('n.','-n.',1)
        s = s.replace('v.','-v.',1)
        s = s.replace('adj.','-adj.',1)
        s = s.replace('prep.','-prep.',1)
        print(s)
        list.append(s)
    write('unit2.txt',list)
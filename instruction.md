# 单词默写需要的python小功能 方法



#### python随机取列表元素不重复

 python避免随机元素重复可以使用random模块的sample()函数，它返回一个新列表，新列表存放随机不重复的元素。 

```python
list = [1, 2, 3]

print(random.sample(list ,2))

list = ["china","python","sky"]

print(random.sample(list ,2))

list = range(1, 10000)

print(random.sample(list ,5))

输出：

[1, 2]

['python', 'sky']

[6912, 1869, 5991, 721, 3388]
```

#### for循环

##### python的for循环从某个变量开始

```
current = 5
for i in range(current,10):
    print(i)
```

##### Python for循环倒序遍历列表

###### 数字列表，range方法构建列表：

```python
for value in range(5, -1, -1):
    print(value)

倒序输出5,4,3,2,1,0

1
2
3
```



###### 文本列表，通过索引值遍历列表：

```python
lists = ['全部', '广州国交润万交通信息有限公司', '广东路路通有限公司','杭州海康威视数字技术股份有限公司', '广东利通科技投资有限公司', '武汉微创光电股份有限公司']
lens = len(lists)-1
for value in range(lens, -1, -1):
    print(lists[value])
```

#### 一招搞定python 去除列表中的\n 和空字符

```python
s=['\n', 'magnet:?xt=urn:btih:060C0CE5CFAE29A48102280B88943880689859FC\n']
上面是目标代码，一个列表，中间有\n，我们现在将其去掉

s=[x.strip() for x in magnet_link]
运行会发现结果为

s=['', 'magnet:?xt=urn:btih:060C0CE5CFAE29A48102280B88943880689859FC']
离我们的要求越来越近了

s=[x.strip() for x in magnet_link if x.strip()!='']
好了，结果出来了

s=['magnet:?xt=urn:btih:060C0CE5CFAE29A48102280B88943880689859FC']
```

